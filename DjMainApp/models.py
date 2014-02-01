from django.db import models

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name="profile")
	pass_reset_code = models.CharField(max_length=200, null=True, blank=True, default=None)
