from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema
from .serializers import LoginSerializer, ProfileSerializer




class LoginView(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(

        request=LoginSerializer
    )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {
                    "message": "Username atau password salah."
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Login berhasil.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                },
            },
            status=status.HTTP_200_OK,
        )


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get Current User",
        description="Retrieve authenticated user profile.",
        responses=ProfileSerializer,
    )

    def get(self, request):
        serializer = ProfileSerializer(request.user)

        return Response(
            {
                "message": "Profile berhasil diambil.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )