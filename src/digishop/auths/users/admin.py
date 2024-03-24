from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from digishop.auths.users.models import User


# Register your models here.

@admin.register(User)
class DigishopUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'verified_email',)