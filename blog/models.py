from django.db import models
import uuid
from writers.models import Profile


class Post(models.Model):
	owner = models.ForeignKey(Profile, null=True, blank=False,
							  on_delete=models.SET_NULL)
	title = models.CharField(max_length=200, null=False, blank=False)
	description = models.TextField(null=False, blank=False)
	image = models.ImageField(null=True, blank=True, default="default.png")
	source = models.URLField(max_length=200, null=True, blank=True)
	tags = models.ManyToManyField('Tag', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
						  primary_key=True, editable=False)

	def __str__(self):
		return self.title


class Review(models.Model):
	VOTE_TYPE = (
		('up', 'Up Vote'),
		('down', 'Down Vote')
	)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	comment = models.TextField(max_length=500, null=True, blank=True)
	value = models.CharField(max_length=200, choices=VOTE_TYPE)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
						  primary_key=True, editable=False)

	def __str__(self):
		return self.value


class Tag(models.Model):
	name = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	id = models.UUIDField(default=uuid.uuid4, unique=True,
						  primary_key=True, editable=False)

	def __str__(self):
		return self.name
