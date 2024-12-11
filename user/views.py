from random import randint
import threading

from django.utils import timezone

from datetime import timedelta

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

from user.models import UserModel
from user.serializers import ResendCodeSerializer, VerifyEmailSerializer, LoginSerializers
from user.utils import send_email_verification


class VerifiyViews(APIView):
    permission_classes = [AllowAny]
    serializer_class = VerifyEmailSerializer

    def post(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        refresh.set_exp(lifetime=timedelta(minutes=30))
        refresh.access_token.set_exp(lifetime=timedelta(minutes=15))
        
        user.last_login = timezone.now()
        user.user_status = 'active'
        user.save()  
        response = {
            "success": True,
            "message": "Email verified successfully",
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
        }

        return Response(response, status=status.HTTP_200_OK)
    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializers
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        full_name = serializer.validated_data.get('full_name', '')  

        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None

        if user:

            verification_code = str(randint(1000, 9999))
            user.verification_code = verification_code
            user.verification_code_created_at = timezone.now()
            user.user_status = 'inactive'
            user.save()

            threading.Thread(target=send_email_verification, args=(user, verification_code)).start()

            return Response({
                "success": True,
                "message": "Verification code sent to the existing user."
            }, status=status.HTTP_200_OK)

        user = UserModel.objects.create_user(
            full_name=full_name,
            email=email,
            username=email.split('@')[0]  
        )
        user.user_status = 'inactive'
        verification_code = str(randint(1000, 9999))
        user.verification_code = verification_code
        user.verification_code_created_at = timezone.now()
        user.save()

        threading.Thread(target=send_email_verification, args=(user, verification_code)).start()

        return Response({
            "success": True,
            "message": "New user created and verification code sent."
        }, status=status.HTTP_201_CREATED)

    
class ResendCodeView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ResendCodeSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Verification code has been resent successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)