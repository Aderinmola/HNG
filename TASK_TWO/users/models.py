import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from .managers import CustomUserManager

# from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(verbose_name=_('userId'), default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(verbose_name=_('firstName'), max_length=255, null=False)
    last_name = models.CharField(verbose_name=_('lastName'), max_length=255, null=False)
    email = models.EmailField(verbose_name=_("email"), unique=True, null=False)
    # phone = PhoneNumberField(verbose_name=_("phone"), max_length=30, default="+2349014153432")
    phone = models.CharField(verbose_name=_("phone"), max_length=30, default="+2349014153432")
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    # "userId": "string" // must be unique
	# "firstName": "string", // must not be null
	# "lastName": "string" // must not be null
	# "email": "string" // must be unique and must not be null
	# "password": "string" // must not be null
	# "phone": "string"

    objects = CustomUserManager()

    class Meta:
        verbose_name=_("User")
        verbose_name_plural=_("Users")

    def __str__(self):
        return self.first_name

