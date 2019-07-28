from rest_framework.permissions import BasePermission


class IsAdminOrRegisterOnly(BasePermission):
    """
    Allows any to register but only admin to manage
    """
    def has_permission(self, request, view):
        if request.method in ['POST']:
            return True
        else:
            return request.user.is_staff
