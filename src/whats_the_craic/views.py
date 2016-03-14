from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from profiles.models import Profile
from registration.models import RegistrationProfile

# Create your views here.

class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	""
		context["submit_btn"] = ""
		return context

class DashboardView(TemplateView):
	template_name = "dashboard.html"

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	""
		context["submit_btn"] = ""		
		user = self.request.user
		profile = Profile.objects.get(user=self.request.user)
		context["profile"] = profile
		print(profile)
		return context