from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only allow access if the user is an admin
        return bool(request.user and request.user.role == 'admin')