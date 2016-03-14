from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import ProfileRegisterForm
from registration.models import RegistrationProfile

# Create your views here.

class ProfileRegister(CreateView):
	model = Profile
	form_class = ProfileRegisterForm	
	success_url = "/accounts/register/complete/"


	def form_valid(self, form):
		#saving the user first
		#user = User.objects.create_user(self.request.POST.get('name'), self.request.POST.get('email'), self.request.POST.get('password'))
		#user = User.objects.create_user(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['password'])
		#user.save()

		user = RegistrationProfile.objects.create_inactive_user(username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
        email=form.cleaned_data['email'],
        site=1)
		
		#creating the profile
		profile = form.save(commit=False)
		#add user_id on profile
		profile.user_id = user.id
		profile.save()
		#saving many to many relationship
		form.save_m2m()

		return HttpResponseRedirect(self.success_url)
	   

	def get_context_data(self, **kwargs):	
		context = super(ProfileRegister, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	"- Add User"
		context["submit_btn"] = "Create Account"
		return context

class ProfileDetailView(DetailView):

	model = Profile

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	"- Add User"
		context["submit_btn"] = "Create Account"
		return context