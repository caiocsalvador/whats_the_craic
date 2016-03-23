from django.conf import settings
from languages.models import Language
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Friendship(models.Model):
	from_user = models.ForeignKey('profiles.Profile', related_name='friendship_requests_sent')
	to_user = models.ForeignKey('profiles.Profile', related_name='friendship_requests_received')
	status = models.BooleanField(default=False)
	
	def __str__(self): #def __unicode__(self):
		return ('%s to %s' % (self.from_user, self.to_user))

