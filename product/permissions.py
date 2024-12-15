from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

class IsManager(BasePermission):
    message = "This page is for managers only"

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.user_type == 'restaurant':
            return True
        raise PermissionDenied(self.message)