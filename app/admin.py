from .models import CustomUser,CompanyMember,Company
from django.contrib import admin
from .action import export_users_to_excel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display=('username','email','first_name','last_name','is_active','is_staff','is_superuser','phone','privaligies')
    list_editable=('email','first_name','last_name','is_active','is_staff','is_superuser','phone','privaligies')
    actions=[export_users_to_excel]

@admin.register(CompanyMember)
class CompanyMemberAdmin(admin.ModelAdmin):
    list_display=('id','user','role','company')
    list_editable=('role',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','name','created_at')
    list_editable=('name',)

