from django.contrib import admin

# Register your models here.

from .models import Friendship

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('from_user', 'to_user', 'status')
	class Meta:
		model = Friendship

admin.site.register(Friendship, FriendshipAdmin)
