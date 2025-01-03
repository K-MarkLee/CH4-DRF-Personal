from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserCreateSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes, authentication_classes


User = get_user_model()
# Create your views here.

@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([])      # 권한 비활성화
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Account created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST']) # POST 요청만 허용
@authentication_classes([])  # 인증 비활성화
@permission_classes([])      # 권한 비활성화
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # 사용자 인증
    user = authenticate(request, username=username, password=password)

    if user is not None: 
        # 인증 성공: 토큰 발급(JWT 토큰 생성)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "message": "Login successful",
        }, status=status.HTTP_200_OK)
    else:
        # 인증 실패
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST']) # POST 요청만 허용
def logout(request):
    try:
        refresh_token = request.data.get('refresh') # refresh 토큰 가져오기 (refresh 토큰이란 access 토큰을 재발급하는 토큰)
        
        token = RefreshToken(refresh_token) # refresh 토큰 생성
        token.blacklist() # 토큰 블랙리스트 추가 (토큰 만료로 로그아웃 처리)

        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
    except:
        refresh_token = request.data.get('refresh')
        print(refresh_token)
        return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET']) # GET, PUT 요청만 허용
def profile(request, username):
    if request.method == 'GET': # GET 요청인 경우 프로필 조회
        user = get_object_or_404(User, username=username)   
        try:
            serializer = ProfileSerializer(user)

        except User.DoesNotExist: # 사용자가 존재하지 않는 경우
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
