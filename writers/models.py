from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.EmailField(max_length=500, blank=True, null=True)
	username = models.CharField(max_length=200, blank=True, null=True)
	short_intro = models.CharField(max_length=200, blank=True, null=True)
	bio = models.TextField(blank=True, null=True)
	profile_image = models.ImageField(null=True, blank=True,
									  upload_to='profiles/',
									  default="profile.png")
	social_facebook = models.URLField(max_length=200, blank=True, null=True)
	social_youtube = models.URLField(max_length=200, blank=True, null=True)
	social_pinterest = models.URLField(max_length=200, blank=True, null=True)
	social_twitter = models.URLField(max_length=200, blank=True, null=True)
	social_instagram = models.URLField(max_length=200, blank=True, null=True)
	social_website = models.URLField(max_length=200, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
						  primary_key=True, editable=False)

	def __str__(self):
		return str(self.user.username)
