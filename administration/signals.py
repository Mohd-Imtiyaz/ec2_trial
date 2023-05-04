from django.db.models.signals import post_save #Import a post_save signal when a user is created
from django.contrib.auth.models import User, Group # Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import Profile, Company_profile
from social_django.models import UserSocialAuth

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_name=instance)

@receiver(post_save, sender=User)
def create_google_auth(sender, instance, created, **kwargs):
    if created:
        UserSocialAuth.objects.create(user=instance, provider='	google-oauth2', uid=instance.email)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=create_google_auth)
def save_google_auth(sender, instance, **kwargs):
    instance.UserSocialAuth.save()

@receiver(post_save, sender=Company_profile)
def create_company(sender, instance, created, **kwargs):
    if created:
        Group.objects.create(name=instance)
        check = Company_profile.objects.filter(company_name = instance)
        check.update(group_name = Group.objects.get(name=instance))
