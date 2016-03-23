from django.conf import settings
from languages.models import Language
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
		print(type(possible_friends))
		#get all profiles who is native at the languages do you want to learn
		teachers = Profile.find_teachers(self)
		print(type(teachers))
		#loop through this profiles and see if they want to learn the native language of this profile
		for teacher in teachers:	
			print(type(teacher))
			for language in teacher.learning.all():
				if self.native == language:					
					possible_friends.add(teacher)
		#now test if they are not friends yet
		for person in possible_friends.copy():
			if(Profile.are_friends(person)):
				possible_friends.remove(person)			
				
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

	def are_friends(self):
		friend = Friendship.objects.filter((Q(from_user=self) | Q(to_user=self)) & Q(status=True))
		if friend:
			return True
		else:
			return False

	def waiting_friendship_approval(self):
		if Friendship.objects.filter((Q(from_user=self) | Q(to_user=self)) & Q(status=False)):
			friend = Friendship.objects.get((Q(from_user=self) | Q(to_user=self)) & Q(status=False))
			if friend:			
				return friend.from_user
		else:
			return False





################# FRIENDSHIP MODEL #######################

class Friendship(models.Model):
	from_user = models.ForeignKey(Profile, related_name="friendship_from_user")
	to_user = models.ForeignKey(Profile, related_name="friendship_to_user")
	status = models.BooleanField(default=False)
	
	def __str__(self): #def __unicode__(self):
		return ('%s to %s' % (self.from_user, self.to_user))