from rest_framework.permissions import BasePermission

class IsAdminOrCreator(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role == "admin" or
            (request.user.role == "creator" and view.action in ['create', 'update', 'partial_update'])
        )

class IsDonor(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "donor"