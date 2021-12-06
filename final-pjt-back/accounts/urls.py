from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
    path('', views.mypage),
    path('<int:user_pk>/follow/', views.follow),
    path('<int:user_pk>/profile/', views.profile),
]