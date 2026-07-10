from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from users.api.serializers import (
    RegisterSerializer,
    UserProfileSerializer
)


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    permission_classes = [
        AllowAny
    ]


class ProfileView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        serializer = UserProfileSerializer(
            request.user
        )

        return Response(
            serializer.data
        )


class LogoutView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        try:

            refresh_token = request.data[
                "refresh_token"
            ]

            token = RefreshToken(
                refresh_token
            )

            token.blacklist()

            return Response(
                {
                    "message":
                    "Logged out successfully."
                },
                status=status.HTTP_200_OK
            )

        except Exception:

            return Response(
                {
                    "error":
                    "Invalid refresh token."
                },
                status=status.HTTP_400_BAD_REQUEST
            )