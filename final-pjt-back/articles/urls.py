from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회
    path('', views.index),
    # 단일 게시글 조회/수정/삭제
    path('<int:article_pk>/', views.article_update_delete),
    # 단일 게시글 생성
    path('create/', views.create),
    # 댓글 조회/생성
    path('<int:article_pk>/comment_create/', views.create_comment),
    # 댓글 수정/삭제
    path('<int:article_pk>/<int:comment_pk>/', views.comment_update_delete),
    # 게시글 좋아요
    path('<int:article_pk>/like/', views.like),
    # 게시글 댓글 좋아요
    path('<int:article_pk>/<int:comment_pk>/like/', views.commentlike),
]