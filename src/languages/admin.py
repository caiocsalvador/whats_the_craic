from django.contrib import admin

# Register your models here.
from .models import Language

class LanguagesAdmin(admin.ModelAdmin):
	class Meta:
		model = Language

admin.site.register(Language, LanguagesAdmin)