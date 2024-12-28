from django.urls import path
from . import views

urlpatterns = [
    path('create_product/', views.create_product, name='create_product'), # 상품 생성
    path('list_products/', views.list_products, name='list_products'), # 상품 목록
]
