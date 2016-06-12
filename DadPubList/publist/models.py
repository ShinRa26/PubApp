from django.db import models

class Pub(models.Model):
	name = models.CharField(max_length=128)
	address = models.CharField(max_length=128)
	area = models.CharField(max_length=128)
	county = models.CharField(max_length=128)
	thisyear = models.BooleanField(default=False)
	fromapp = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name
