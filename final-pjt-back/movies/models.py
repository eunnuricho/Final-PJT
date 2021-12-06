from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateField(null=True)
    genre_ids = models.ManyToManyField(Genre)
    poster_path = models.CharField(max_length=200, null=True)
    vote_count = models.PositiveIntegerField()
    vote_average = models.FloatField()

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=100)
    movie_pk = models.IntegerField()
    rank = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review_comments')

    def __str__(self):
        return self.content
