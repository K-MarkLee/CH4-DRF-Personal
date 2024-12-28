from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'), # 회원가입
    path('login/', views.login, name='login'), # 로그인
    path('logout/', views.logout, name='logout'), # 로그아웃
    
    path('profile/<str:username>/', views.profile, name='profile'), # 프로필
]
