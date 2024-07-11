import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Organisation(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(verbose_name=_('orgId'), default=uuid.uuid4, editable=False, unique=True)
    user = models.ManyToManyField(User, related_name="organisation_users")
    name = models.CharField(verbose_name=_('name'), max_length=255, null=False)
    description = models.TextField(verbose_name=_('description'))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    #     {
    # 	"orgId": "string", // Unique
    # 	"name": "string", // Required and cannot be null
    # 	"description": "string",
    # }

    def __str__(self):
        return self.name
