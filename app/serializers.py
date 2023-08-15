from rest_framework import serializers
from .models import *




class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
        )
class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'created_at',
        )



class CompanyMemberListSerializer(serializers.ModelSerializer):
    user=CustomUserListSerializer(many=False,read_only=True)
    class Meta:
        model = CompanyMember
        fields = (
            'company',
            'id',
            'role',
            'company',
            'user',
        )



class CompanyMemberListIdSerializer(serializers.ModelSerializer):
    company=CompanyListSerializer(many=False,read_only=True)
    user=CustomUserListSerializer(many=False,read_only=True)
    class Meta:
        model = CompanyMember
        fields = (
            'id',
            'company',
            'user',
            'role',
        )