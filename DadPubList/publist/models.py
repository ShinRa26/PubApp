from django.db import models
from django.template.defaultfilters import slugify

class Pub(models.Model):
	name = models.CharField(max_length=128, unique=False)
	slug = models.SlugField()
	address = models.CharField(max_length=128)
	area = models.CharField(max_length=128)
	county = models.CharField(max_length=128)
	thisyear = models.BooleanField(default=False)
	fromapp = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Pub, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name
