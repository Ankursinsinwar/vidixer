from rest_framework import permissions

class IsClientOrReadOnly(permissions.BasePermission):
    """
    Allow only clients to create/update projects.
    Editors can only view assigned projects.
    """

    def has_permission(self, request, view):
        # Allow safe (GET, HEAD, OPTIONS) requests to everyone logged in
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        # Only allow POST/PUT/DELETE if user is a client
        return request.user.is_authenticated and request.user.role == 'client'
