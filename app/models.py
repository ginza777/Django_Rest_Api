from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Choice(models.TextChoices):
    customer = 'customer',
    admin = 'admin',
    manager = 'manager',
    employee = 'employee'
    teacher = 'teacher'
    block = 'block'
    test = 'test'


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True)
    email = models.EmailField(max_length=150)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    phone = PhoneNumberField(blank=True, null=True)
    privaligies = models.CharField(max_length=150, choices=Choice.choices, default=Choice.customer)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name_plural = 'CustomUser'
        db_table = 'GinzaAuthUser_customuser'

    def __str__(self):
        return self.username


class CompanyMemberRole(models.TextChoices):
    admin = 'admin',
    founder = 'founder',
    employee = 'employee'

class CompanyMember(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    role=models.CharField(max_length=150,choices=CompanyMemberRole.choices,default=Choice.employee)
    company=models.ForeignKey('Company',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



class Company(models.Model):
    name=models.CharField(max_length=150)
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name