from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import Genre, Movie, Review, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = '__all__'
    
    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'genre_ids', 'overview', 'release_date', 
        'poster_path', 'vote_count', 'vote_average',
        )


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name')


class ReviewSerializer(serializers.ModelSerializer):

    # class MovieListSerializer(serializers.ModelSerializer):
        
    #     class Meta:
    #         model = Movie
    #         fields = ('pk', 'title',)

    # movie_title = MovieListSerializer(write_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        depth = 1
        read_only_fields = ('user', 'like_users')


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'content', 'created_at', 'updated_at',  )
        read_only_fields = ( 'review', 'user','like_users', ) 


class MovieRecommendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title',)


class CommentsRelatedReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at', ]



class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments = CommentsRelatedReviewSerializer(many=True)
    like_users = UserSerializer(many=True)
    class Meta:
        model = Review
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'like_users', 'comments']


class UserReviewSerializer(UserSerializer):
    reviews = ReviewListSerializer(many=True)
    like_reviews = ReviewListSerializer(many=True)
    comments = CommentsRelatedReviewSerializer(many=True)
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ['reviews', 'like_reviews', 'comments']