from django.db import models

# Create your models here.

class Language(models.Model):	
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10)

	def __str__(self): #def __unicode__(self):
		return self.name