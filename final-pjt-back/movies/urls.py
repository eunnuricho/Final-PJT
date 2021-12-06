from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # 전체 영화 목록 조회
    path('', views.getmovie),
    # 단일 영화 상세 조회
    path('<int:movie_pk>/', views.movie_detail),
    # 전체 리뷰 조회
    path('community/', views.getreview),
    # 리뷰 생성
    path('community/create/', views.create_review),
    # 리뷰 단일 조회/수정/삭제
    path('community/<int:review_pk>/', views.review_update_delete),
    # 리뷰 좋아요
    path('community/<int:review_pk>/like/', views.like),
    # 댓글 생성
    path('community/<int:review_pk>/comment_create/', views.create_comment),
    # 댓글 단일 조회/수정/삭제
    path('community/<int:review_pk>/<int:comment_pk>/', views.comment_update_delete),
    
    # 영화 추천
    path('recommend/', views.recommend),

    # 리뷰 댓글 좋아요
    path('community/<int:review_pk>/<int:comment_pk>/like/', views.commentlike),
]