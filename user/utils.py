from django.core.mail import EmailMultiAlternatives

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.utils import timezone

from datetime import timedelta


def send_email_verification(user, verification_code):
        text_content = f"""Your verification code is: {verification_code}
        Verification code will expire after 2 minutes"""
        message = EmailMultiAlternatives(
            subject="Verification Code",
            body=text_content,
            to=[user.email],
            from_email="abubakrrahmatullayev1001@gmail.com"   
        )
        message.send()


def generate_tokens(user, message, user_type: str):
    user.user_status = 'active'
    user.user_type = user_type
    user.save()

    refresh = RefreshToken.for_user(user)
    refresh.set_exp(lifetime=timedelta(minutes=30))
    refresh.access_token.set_exp(lifetime=timedelta(minutes=15))

    user.last_login = timezone.now()
    user.user_status = 'active'
    user.save()

    response = {
        "success": True,
        "message": message,
        "refresh_token": str(refresh),
        "access_token": str(refresh.access_token),
    }
    return Response(response, status=status.HTTP_200_OK)