# users/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User # sender
from django.dispatch import receiver    # receiver
from .models import Profile

@receiver(post_save, sender=User)   # when a user is saved, send the signal which is post_save, the signal sends create_profile
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)   # when a user is saved, send the signal which is post_save, the signal sends save_profile
def save_profile(sender, instance, **kwargs):
    instance.profile.save()