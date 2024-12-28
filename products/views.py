from .models import Product
from rest_framework import status
from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['POST']) # POST 요청만 허용
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(author=request.user) # 작성자 추가 (현재 로그인한 유저)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET']) # GET 요청만 허용
def list_products(request):
    products = Product.objects.all().order_by("created_at") # 모든 상품 조회 (작성일 기준)
    serializer = ProductSerializer(products, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK) # 상품 목록 반환
