from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes



# Create your views here.

@api_view(['POST'])
@authentication_classes([])  # 인증 비활성화
@permission_classes([])      # 권한 비활성화
def create_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Account created successfully."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
