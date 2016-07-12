from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from profiles.models import Profile
from registration.models import RegistrationProfile
import json

# Create your views here.

class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	""
		context["submit_btn"] = ""
		return context

class DashboardView(SuccessMessageMixin, TemplateView):
	template_name = "dashboard.html"

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)

		#TESTS WE NEED
		user = self.request.user
		profile = Profile.objects.get(user=self.request.user)
		friendships_requests = profile.find_friendships_requests()
		friends = profile.get_friends()
		new_messages_count = profile.get_new_messages_count()

		#ALL CONTEXT VARIABLES
		context["profile"] = profile
		context["friendships_requests"] = friendships_requests
		context["friends"] = friends
		context["new_messages_count"] = new_messages_count
		context["site_name"] = 	"What's the Craic?"
		context["title"] = 	""
		context["submit_btn"] = ""
		return context

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

class Contact(SuccessMessageMixin, View):
	template_name = "add_friend.html"

	def dispatch(self, request, *args, **kwargs):
		print("entrei")
		response_data = {}
		name = request.POST.get('name')
		email = request.POST.get('email')
		message = request.POST.get('message')
		response_data['send'] = send_mail('Contact from Whats the Craic? Website', 'Name:'+name+'<br>Message:'+message, email,
    	['caiocsalvador@gmail.com'], fail_silently=False)

		return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )