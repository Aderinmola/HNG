from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ["pkid", "id", "email", "first_name","last_name"]
    list_display_links=["id", "email"]
    list_filter=["email", "first_name","last_name"]

admin.site.register(User, UserAdmin)
