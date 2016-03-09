from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stories(models.Model):
	title = models.CharField(max_length=50, unique=True)
	link = models.CharField(max_length=100, unique=True)
	created_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title


class Comment(models.Model):
	story = models.ForeignKey(Stories)
	comment = models.CharField(max_length=250, blank=True, null=True)


class Vote(models.Model):
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)
	story = models.ForeignKey(Stories)

	