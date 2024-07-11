from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
# from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    ordering = ["-created_at"]
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = Organisation
    list_display = ["pkid", "id", "name", "description","created_at", "updated_at"]
    

admin.site.register(Organisation, OrganisationAdmin)
