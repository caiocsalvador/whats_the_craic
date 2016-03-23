from django.conf import settings
from languages.models import Language
from friendships.models import Friendship
from django.db import models
from django.db.models import Q
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

	#Find possible friends
	def find_friends(self):
		possible_friends = set()

		#get all profiles who is native at the languages do you want to learn
		can_teach = Profile.find_teachers(self)
		#loop through this profiles and see if they want to learn the native language of this profile
		for profile in can_teach:	
			for language in profile.learning.all():
				if self.native == language:					
					possible_friends.add(profile)
		#now test if they are not friends yet
		for possible_friend in possible_friends.copy():
			if(Profile.are_friends(possible_friend)):
				possible_friends.remove(possible_friend)			
				
		return possible_friends

    
	def is_native(self, language):
		if self.native == language:
			return True
		else:
			return False

	#get all profiles who is native at the languages do you want to learn
	def find_teachers(self):
		for language in self.learning.all():
			can_teach = Profile.objects.filter(native=language)
		return can_teach  

	def are_friends(possible_friend):
		friends = Friendship.objects.filter(Q(from_user=possible_friend) | Q(to_user=possible_friend))
		if friends:
			return True
		else:
			return False

