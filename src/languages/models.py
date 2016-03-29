from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

def download_media_location(instance, filename):
	fname, dot, extension = filename.rpartition('.')
	slug = slugify(fname)
	return '%s/%s.%s' % (instance.code, slug, extension)  

class Language(models.Model):	
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10)
	flag = models.ImageField(
		blank=True,
		null=True,
		upload_to=download_media_location
		) #, storage=FileSystemStorage(location=settings.PROTECTED_ROOT)

	def __str__(self): #def __unicode__(self):
		return self.name