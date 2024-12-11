import random
import threading

from rest_framework import serializers

from user.models import UserModel
from user.utils import send_email_verification

from django.utils import timezone

from datetime import timedelta

    
class LoginSerializers(serializers.Serializer):
    full_name = serializers.CharField(max_length=255, allow_blank=True)
    email = serializers.EmailField(max_length=255, required=False)


    def validate_email(self, email: str):
        email = email.strip()
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise serializers.ValidationError("Invalid email format. Please enter a valid email address.")
        return email
    
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)  
        user.user_status = 'inactive' 
        user.save()
        return user 
    

    def generate_verification_code(self):
        self.verification_code = str(random.randint(1000, 9999))  
        self.verification_code_created_at = timezone.now()  
        self.save()
        return self.verification_code  


class VerifyEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    verification_code = serializers.CharField(max_length=4, required=True)

    def validate(self, data):
        email = data.get('email')
        verification_code = data.get('verification_code')
        
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("User not found!")
        if user.verification_code != verification_code:
            raise serializers.ValidationError("Invalid verification code!")
        
        current_time = timezone.now()
        if user.verification_code_created_at + timedelta(minutes=2) < current_time:
            raise serializers.ValidationError("Verification code expired!")
        
        data['user'] = user 
        return data
    

class ResendCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("User not found!")
        
        user.verification_code = str(random.randint(1000, 9999))  
        user.verification_code_created_at = timezone.now() 
        user.save()
        
        threading.Thread(target=send_email_verification, args=(user, user.verification_code)).start()
        
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        exclude = ['password', 'groups', 'user_permissions', 'is_superuser']
        read_only_fields = ['is_active', 'date_joined', 'last_login', 'is_staff']

    def validate(self, attrs):
        user = self.context['request'].user
        to_user = attrs['to_user']
        if to_user == user:
            raise serializers.ValidationError("You can't follow yourself.")
        return attrs