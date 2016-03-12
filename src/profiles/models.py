from django.conf import settings
from languages.models import Language
from django.db import models
from django.template.defaultfilters import slugify

def download_media_location(instance, filename):
	fname, dot, extension = filename.rpartition('.')
	slug = slugify(fname)
	return '%s/%s.%s' % (instance.user.id, slug, extension)  

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	nui_id = models.IntegerField(unique=True)
	staff = models.BooleanField(default=True)
	native = models.ForeignKey(Language)
	learning = models.ManyToManyField(Language, related_name="profile_languages")
	picture = models.ImageField(
		blank=True,
		null=True,
		upload_to=download_media_location
		) #, storage=FileSystemStorage(location=settings.PROTECTED_ROOT)

	def __str__(self): #def __unicode__(self):
		return self.name


      