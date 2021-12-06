from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Article, ArticleComment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','age']


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('pk', 'title', )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        depth = 1
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ('id', 'content', 'created_at', 'updated_at', )
        read_only_fields = ('article', 'user', 'like_users')


class CommentsRelatedArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = ArticleComment
        fields = ['id', 'user', 'content', 'created_at', ]


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentsRelatedArticleSerializer(many=True)
    like_users = UserSerializer(many=True)
    class Meta:
        model = Article
        fields = ['id', 'movie', 'user', 'title', 'content', 'rank', 'created_at', 'updated_at', 'like_users', 'comments']


class UserArticleSerializer(UserSerializer):
    articles = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)
    comments = CommentsRelatedArticleSerializer(many=True)
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['articles', 'like_articles', 'comments']