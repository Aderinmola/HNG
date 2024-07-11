from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from core.settings import AUTH_USER_MODEL
from .models import Organisation

User = get_user_model()

@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_organization(sender, instance, created, **kwargs):

    if created:
        print("INSTANCE", instance.last_name)
        # user=User.objects.get(id=instance)
        # Organisation.objects.create(name=f"{instance.organisation_users.first_name}'s Organization", user=instance)
        organisation =Organisation.objects.create(name=f"{instance.first_name}'s Organization")
        organisation.user.set([instance])



# @receiver(post_save, sender=AUTH_USER_MODEL)
# def save_user_organisation(sender, instance, **kwargs):
#     instance.organisation_users.save()
#     print(f"{instance}'s organisation created!!!!!")
