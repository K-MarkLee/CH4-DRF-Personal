from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields): # 사용자 생성
        if not email:
            raise ValueError('Email is required.')
        if not username:
            raise ValueError('Username is required.')

        email = self.normalize_email(email) # 이메일 소문자로 변경
        user = self.model(email=self.normalize_email(email),username=username, **extra_fields) 
        user.set_password(password)
        user.save(using=self._db) # using=self._db는 여러 데이터베이스를 사용할 때 사용
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        return self.create_user(email, username, password, **extra_fields)
    


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True) # 이메일 필드
    username = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)]) # username 필드 (id로 사용) / MinLengthValidator(3)은 최소 3글자 이상
    name = models.CharField(max_length=50) # 이름 필드
    nickname = models.CharField(max_length=30) # 닉네임 필드
    birth_date = models.DateField() # 생년월일 필드
    gender = models.CharField(max_length=10, blank=True, null=True) # 성별 필드 (선택사항)
    bio = models.TextField(blank=True, null=True) # 자기소개 필드 (선택사항)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True) # 프로필 이미지 필드 (선택사항)
 
    objects = CustomUserManager() # CustomUserManager를 사용하여 사용자 생성

    USERNAME_FIELD = 'username' # username을 사용하여 로그인
    REQUIRED_FIELDS = ['email', 'name', 'nickname', 'birth_date'] # 필수로 입력해야 하는 필드

    def __str__(self):
        return self.username # username을 반환