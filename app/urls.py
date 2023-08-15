from django.urls import path

from .views import *

urlpatterns = [
    path('userlist/', CustomUserList.as_view(), name='register'),
    path('userlist/excel/', CustomUserListExcel.as_view(), name='register'),
    path('companylist/', CompanyList.as_view(), name='register'),
    path('companymemberlist/', CompanyMemberList.as_view(), name='register'),
    path('companymemberlist/<int:company_id>/', CompanyMemberListId.as_view(), name='register'),


    ]
