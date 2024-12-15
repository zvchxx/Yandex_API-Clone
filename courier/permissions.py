from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

class IsCourier(BasePermission):
    message = "This page is for courier only"

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == 'courier':
            return True
        raise PermissionDenied(self.message)