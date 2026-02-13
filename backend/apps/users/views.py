# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registration request received"},
                status=status.HTTP_201_CREATED,
            )
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(f"Request data: {request.data}")
        return Response({"message": "User login request received"})
