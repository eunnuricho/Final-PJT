from django.http import response
from django.http.response import HttpResponse
from django.views.decorators.http import require_safe
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import serializers
from .models import Movie, Review, Comment
from .serializers import (MovieListSerializer, ReviewListSerializer, 
ReviewSerializer, CommentSerializer, MovieRecommendSerializer)
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework import status
import random

#전체 movie 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def getmovie(request):
    movies = Movie.objects.order_by('-release_date')[30:500]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

#단일 영화 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

# 전체 review 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def getreview(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# 단일 review 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request):
    print(request.data)
    # movie = get_object_or_404(Movie, pk=pk)
    serializer = ReviewSerializer(data=request.data)
    print(serializer)
    print('1111111111111111111111111111')
    if serializer.is_valid(raise_exception=True):        
        serializer.save(user=request.user)
        print(serializer.data)
        print('222222222222222222222222222222')
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# def create_review(request):
#     serializer = ReviewSerializer(data=request.data)
#     # print(serializer.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 review 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = ReviewSerializer(review, data=request.data)
        print(serializer)
        if not request.user.reviews.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        if not request.user.reviews.filter(pk=review_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response({ 'id': review_pk }, status=status.HTTP_204_NO_CONTENT)


# comment 목록 조회, 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = review.comments.order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print(request.data)
        print(review)
        serializer = CommentSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            print('11111')
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 단일 comment 조회, 수정, 삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, comment_pk, review_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        print(serializer)
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        if not request.user.comments.filter(pk=comment_pk).exists():
            return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()
        data = {
            'id': comment_pk,
            'delete': f'data {comment_pk} is deleted!!',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    reviews = get_list_or_404(Review)
    pk_list = []
    random_num = 0
    for review in reviews:
        if request.user == review.user:
            if review.rank >= 3:
                pk_list.append([review.movie_pk, review.rank])

    arr = []
    max_rank = 0
    if len(pk_list) >= 1:
        for i in range(len(pk_list)):
            if pk_list[i][1] >= max_rank:
                max_rank = pk_list[i][1]
        for i in range(len(pk_list)):
            if pk_list[i][1] == max_rank:
                arr.append(pk_list[i][0])
    
    if len(arr) >= 2:
        aa=random.sample(arr, 1)
        random_num += aa[0]
        movie = Movie.objects.filter(pk=random_num).first()
        serializer = MovieRecommendSerializer(movie)
        return Response(serializer.data)
    
    elif len(arr) == 1:
        random_num += arr[0]
        movie = Movie.objects.filter(pk=random_num).first()
        serializer = MovieRecommendSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    if user in review.like_users.all():
        review.like_users.remove(user)
        liked = False
    else:
        review.like_users.add(user)
        liked = True
    return Response({
        "liked": liked,
        "count": review.like_users.count()
    })


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def commentlike(request, review_pk, comment_pk):
    user = request.user

    comment = get_object_or_404(Comment, pk=comment_pk)
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