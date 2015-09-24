from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tag(models.Model):
	title = models.CharField(max_length=500)

	def __str__(self):
		return self.title

class Post(models.Model):
	user = models.ForeignKey(User)
	img = models.CharField(max_length=500, null=True, blank=True)
	title = models.CharField(max_length=500)
	content = models.TextField()
	tags = models.ManyToManyField(Tag)
	created = models.DateTimeField()
	updated = models.DateTimeField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	content = models.TextField()
	created = models.DateTimeField()

	def __str__(self):
		return self.content