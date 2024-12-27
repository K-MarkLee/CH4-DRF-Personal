from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields): # 사용자 생성 함수
        if not username: # 사용자 이름이 없는 경우
            raise ValueError('The Username field is required.')
        if not email: # 이메일이 없는 경우
            raise ValueError('The Email field is required.')

        email = self.normalize_email(email) # 이메일 소문자로 변경
        user = self.model(username=username, email=email, **extra_fields) # 사용자 생성
        user.set_password(password) # 비밀번호 설정
        user.save(using=self._db) # 저장(using = self._db 는 여러 데이터베이스를 사용하는 경우에 필요)
        return user


    def create_superuser(self, username, email, password=None, **extra_fields): # 슈퍼유저 생성 함수
        extra_fields.setdefault('is_staff', True) # 스태프 권한 부여
        extra_fields.setdefault('is_superuser', True) # 슈퍼유저 권한 부여

        if extra_fields.get('is_staff') is not True: # 스태프 권한이 없는 경우
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True: # 슈퍼유저 권한이 없는 경우
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username=username, email=email, password=password, **extra_fields) # 사용자 생성


class User(AbstractUser, PermissionsMixin): 
    email = models.EmailField(unique=True)  # 이메일 필드
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)])  # 아이디로 사용할 username 필드 / MinLengthValidator(3)은 최소 3글자 이상
    name = models.CharField(max_length=50)  # 이름 필드
    nickname = models.CharField(max_length=30)  # 닉네임 필드
    birth_date = models.DateField()  # 생년월일 필드
    gender = models.CharField(max_length=10, blank=True, null=True)  # 성별 필드
    bio = models.TextField(blank=True, null=True)  # 자기소개 필드
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # 프로필 이미지

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # username을 로그인 필드로 사용
    REQUIRED_FIELDS = ['email', 'name', 'nickname', 'birth_date']  # 필수 입력 필드 설정

    def __str__(self):
        return self.username
