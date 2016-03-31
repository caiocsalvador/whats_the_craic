from django.contrib import admin

# Register your models here.

from .models import Friendship, Profile, Message

class ProfilesAdmin(admin.ModelAdmin):
	class Meta:
		model = Profile

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('from_user', 'to_user', 'status')
	class Meta:
		model = Friendship

class MessageAdmin(admin.ModelAdmin):
	list_display = ('from_user', 'to_user')
	class Meta:
		model = Friendship


admin.site.register(Profile, ProfilesAdmin)
admin.site.register(Friendship, FriendshipAdmin)
admin.site.register(Message, MessageAdmin)