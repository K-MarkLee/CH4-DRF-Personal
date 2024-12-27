# serializers.py

from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'password2', 'username', 'profile_image')

        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                'password': 'Password incorrect.'
            })
        return data
    


    def create(self, validated_data):
        user = get_user_model()
        validated_data.pop('password2')
        return user.objects.create_user(**validated_data)
    

