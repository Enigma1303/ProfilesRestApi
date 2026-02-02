from rest_framework import permissions


class updateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Verify if user is only editing their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        """Same Id of object and logged in user"""
        return obj.id== request.user.id