from django.db.models.signals import post_save

from django.contrib.auth.models import User

from django.dispatch import receiver

from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender, instances, created, **kwargs):
    if created:
        Profile.objects.create(user=instances)


@receiver(post_save,sender=User)
def create_profile(sender, instances, **kwargs):
    instances.profile.save()