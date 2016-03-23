from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from .forms import ProfileRegisterForm
from registration.models import RegistrationProfile


#messagescreate
#def form_valid(self, form):
#	user = self.request.user
#	form.instance.user = user
#	valid_data = super(nomedaview, self).form_valid(form)
#	adicione qq coisa apos a mensagem criada
#	return valid_data

# Create your views here.

### CREATE ###
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
		context["title"] = 	"- Add Profile"
		context["submit_btn"] = "Create Account"
		return context

### UPDATE ###
class ProfileUpdate(SuccessMessageMixin, UpdateView):
	model = Profile
	#form_class = ProfileRegisterForm#	
	fields = ['name', 'picture', 'nui_id', 'staff', 'native', 'learning']
	success_url = "/dashboard/"
	template_name = 'profiles/profile_edit.html'
	success_message = "Profile was updated successfully" 
			

	def dispatch(self, request, *args, **kwargs):
		user = self.request.user
		obj = self.get_object()
		if obj.user != user:
			messages.error(self.request, 'This profile is not yours.')
			return HttpResponseRedirect(reverse('dashboard'))
		return super(ProfileUpdate, self).dispatch(request, *args, **kwargs)


	def get_context_data(self, **kwargs):	
		context = super(ProfileUpdate, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	"- Update Profile"
		context["submit_btn"] = "Update Account"
		return context


class ProfileDetailView(DetailView):

	model = Profile

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		user = self.request.user
		profile = Profile.objects.get(user=self.request.user)
		are_friends = profile.are_friends()
		waiting = profile.waiting_friendship_approval()
		if waiting:
			if profile == waiting:
				context["waiting"] = "waiting approval"
			else:
				context["waiting"] = "accept request"

		context["profile"] = profile
		context["are_friends"] = are_friends
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	"- Add User"
		context["submit_btn"] = "Create Account"
		return context


class FindFriends(SuccessMessageMixin, TemplateView):
	template_name = "findfriends.html"

	def get_context_data(self, **kwargs):
		context = super(FindFriends, self).get_context_data(**kwargs)

		#TESTS WE NEED
		user = self.request.user
		profile = Profile.objects.get(user=self.request.user)
		possible_friends = Profile.find_friends(profile)

		#ALL CONTEXT VARIABLES
		context["profile"] = profile
		context["possible_friends"] = possible_friends
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	""
		context["submit_btn"] = ""
		return context


class AddFriend(SuccessMessageMixin, TemplateView):
	template_name = "add_friend.html"

	#def dispatch(self, request, *args, **kwargs):
		#print(self.kwargs['pk'])
		#user = self.request.user
		#obj = self.get_object()
		#if obj.user != user:
			#messages.error(self.request, 'This profile is not yours.')
			#return HttpResponseRedirect(reverse('dashboard'))
		#return super(ProfileUpdate, self).dispatch(request, *args, **kwargs)
		
