from re import M
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, UserReviewArticleSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.decorators import api_view
from .models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    print('12312313123123')
    print(request.data)
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.(write_only)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 마이페이지
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def mypage(request):
    user = request.user
    serializer = UserReviewArticleSerializer(user)
    return Response(serializer.data)

# 유저 프로필
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)


# 팔로우
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
#username으로 해야할수도............아닌듯......
def follow(request, user_pk):
    me = request.user
    you = get_object_or_404(User, pk=user_pk)
    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            followed = False

        else:
            you.followers.add(me)
            followed = True
        
        return Response({
            'followed': followed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        })
