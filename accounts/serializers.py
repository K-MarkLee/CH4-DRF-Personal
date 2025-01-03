from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])  # 비밀번호 필드
    password2 = serializers.CharField(write_only=True, required=True)  # 비밀번호 확인 필드

    class Meta:
        model = User # User 모델 사용
        fields = ['email', 'username', 'password', 'password2', 'name', 'nickname', 'birth_date', 'gender', 'bio', 'profile_image'] # 필드


    def validate(self, data): # 입력값 유효성 검사 함수
        if data['password'] != data['password2']: # 비밀번호와 비밀번호 확인이 다를 경우
            raise serializers.ValidationError({"password": "Passwords do not match."})
        
        if User.objects.filter(email=data['email']).exists(): # 이메일이 이미 존재하는 경우
            raise serializers.ValidationError({"email": "Email already exists."})
        
        if User.objects.filter(username=data['username']).exists(): # 사용자 이름이 이미 존재하는 경우
            raise serializers.ValidationError({"username": "Username already exists."})
        
        # 생년월일 형식 확인
        try:
            datetime.strptime(str(data['birth_date']), '%Y-%m-%d')  # YYYY-MM-DD 형식 확인
        except ValueError:
            raise serializers.ValidationError({"birth_date": "Birth date must be in the format YYYY-MM-DD."})

        return data

    def create(self, validated_data):
        validated_data.pop('password2') # 비밀번호 2는 검증용이라 필요 없기에 제거
        user = User.objects.create_user(**validated_data) # 사용자 생성
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'nickname', 'birth_date', 'gender', 'bio', 'profile_image'] # 공개 필드