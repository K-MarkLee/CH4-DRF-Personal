from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'), # 회원가입
    path('login/', views.login, name='login'), # 로그인
]
