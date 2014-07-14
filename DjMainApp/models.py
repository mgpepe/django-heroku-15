from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



"""
# Uncomment those lines after you have synced your database to get user profile functionality
##############################################################

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	pass_reset_code = models.CharField(max_length=200, null=True, blank=True, default=None)

# Create automatically a User Profile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
"""
