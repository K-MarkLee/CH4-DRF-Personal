from rest_framework import status  
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import CreateSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, authentication_classes, permission_classes




# Create your views here.
@api_view(['POST'])
@authentication_classes([])      # settings 의 authentication_classes 무시
@permission_classes([])  # settings 의 permission_classes 무시
def create(request):
    serializer = CreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message" : "Signup Success"
        }, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@authentication_classes([]) 
@permission_classes([]) 
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # JWT 토큰 생성
            refresh = RefreshToken.for_user(user)
            return JsonResponse({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'message': '로그인 성공'
            }, status=200)
        else:
            return JsonResponse({'error': 'Something is wrong. Try agin'}, status=400)
        


@api_view(['POST'])
@authentication_classes([])
@permission_classes([]) 
def logout(request):
    print('---')
    try:
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"error": "need refresh_token."}, status=status.HTTP_400_BAD_REQUEST)
        
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Log out"})
    
    except Exception:
        return Response({"error": "Log out Failed"}, status=status.HTTP_400_BAD_REQUEST)