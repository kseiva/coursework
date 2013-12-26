from django.db import models
import os

class Gallery(models.Model):
	original = models.ImageField(upload_to = 'uploads/original')
	title = models.CharField(max_length = 100)

	def __unicode__(self):
		return self.title

	def preview(self):
		path, f = os.path.split(self.original.name)
		return "uploads/preview/" + f