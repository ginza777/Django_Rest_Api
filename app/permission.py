from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission
from rest_framework.status import HTTP_401_UNAUTHORIZED

from app.management.commands.data import CompanyMemberRole
from app.models import CompanyMember


class IsFounderPermission(BasePermission):
    def has_permission(self, request, view):
        # Check if the user's role is 'founder' within the CompanyMember
        if request.user.is_authenticated:
            return CompanyMember.objects.filter(user=request.user, role='founder').exists()
        return False
