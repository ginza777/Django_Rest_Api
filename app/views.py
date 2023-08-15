from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView, ListAPIView,GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
import django_filters
from app.models import CustomUser
from .exel import export_users_to_excel
from .permission import IsFounderPermission
from .serializers import *
#import pagination
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'  # Allow client to request a specific page size
    max_page_size = 100  # Set the maximum page size


class CustomUserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination


class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

class CompanyMemberList(ListAPIView):
    queryset = CompanyMember.objects.all()
    serializer_class = CompanyMemberListSerializer
    permission_classes = (IsAuthenticated,IsFounderPermission)
    pagination_class = CustomPagination

    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['user__username',
                     'user__first_name',
                     'user__last_name',
                     'user__email',
                     'company__name'
                     ]
    filterset_fields = [ 'role']  # Add fields for filtering



class CompanyMemberListId(ListAPIView):
    serializer_class = CompanyMemberListIdSerializer
    permission_classes = (IsAuthenticated,IsFounderPermission)
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'company__name']
    filterset_fields = ['role']  # Add fields for filtering
    def get_queryset(self):
        company_id=self.kwargs['company_id']
        return CompanyMember.objects.filter(company__id=company_id)

class CustomUserListExcel(GenericAPIView):

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()  # Get your queryset as needed
        filename = 'user_data.xls'

        export_users_to_excel(users, filename)

        # You can return the Excel file as a response
        with open(filename, 'rb') as excel_file:
            response = HttpResponse(excel_file.read(), content_type='application/ms-excel')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response