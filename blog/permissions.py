

from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


# burada özel bir permission tanımlıyoruz. BasePermission dan overread ederek.
class IsAdminOrReadOnly(BasePermission):
    # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    """
    The request is authenticated as a user, or is a read-only request.
    """
    # kullancı admin ise crud işlemine izin ver yoksa sadece get işlemi yapsın
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff # kullanıcı admin mi anlamında
        )
