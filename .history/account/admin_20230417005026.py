from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from account.models import CustomUserModel

class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username','email')

# Register your models here.
