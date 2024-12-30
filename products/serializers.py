from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'author', 'title', 'content', 'image', 'created_at', 'updated_at'] # 필드
        read_only_fields = ['id', 'author', 'created_at', 'updated_at'] # 읽기 전용 필드

    def validate(self, data):

        if not data.get('image'):
            raise serializers.ValidationError({"image": "An image is required for this product."})
        
        if 'image' in data and data['image'] is None:
            raise serializers.ValidationError({"image": "An image is required for this product."})
        return data