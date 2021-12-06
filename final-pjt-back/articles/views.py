from django.http import response
from django.http.response import HttpResponse
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers
from .models import Article, ArticleComment
from .serializers import (ArticleSerializer, CommentSerializer)
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import status

#전체 article 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# 단일 article 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 단일 article 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def article_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        # serializer = UserArticleSerializer(user)
        # return Response(serializer.data)
    # 수정
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if not request.user.articles.filter(pk=article_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 삭제
    elif request.method == 'DELETE':
        if not request.user.articles.filter(pk=article_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        article.delete()
        return Response({ 'id': article_pk }, status=status.HTTP_204_NO_CONTENT)


# comment 목록 조회, 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 댓글 목록 조회
    if request.method == 'GET':
        comments = article.comments.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # 댓글 생성
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 comment 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk, article_pk):
    comment = get_object_or_404(ArticleComment, pk=comment_pk)
    # 댓글 조회
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        
        if not request.user.article_comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    # 댓글 삭제
    elif request.method == 'DELETE':
        if not request.user.article_comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        data = {
            'id': comment_pk,
            'delete': f'data {comment_pk} is deleted!!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    if user in article.like_users.all():
        article.like_users.remove(user)
        liked = False
    else:
        article.like_users.add(user)
        liked = True
    return Response({
        "liked": liked,
        "count": article.like_users.count()
    })

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def commentlike(request, article_pk, comment_pk):
    user = request.user

    comment = get_object_or_404(ArticleComment, pk=comment_pk)
    serializer = CommentSerializer(comment)

    print(serializer.data)

    if user in comment.like_users.all():
        comment.like_users.remove(user)
        liked = False
    else:
        comment.like_users.add(user)
        liked = True

    return Response({
        "liked": liked,
        "count": comment.like_users.count()
    })