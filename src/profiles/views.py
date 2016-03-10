from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import ProfileRegisterForm

# Create your views here.


class ProfileRegister(CreateView):
	model = Profile
	form_class = ProfileRegisterForm	
	success_url = "/"


	def form_valid(self, form):
		#saving the user first
		user = User.objects.create_user(self.request.POST.get('name'), self.request.POST.get('email'), self.request.POST.get('password'))
		user.save()
		#creating the profile
		profile = form.save(commit=False)
		#add user_id on profile
		profile.user_id = user.id
		profile.save()
		#saving many to many relationship
		form.save_m2m()

		return HttpResponseRedirect(self.success_url)
	   

	#def form_valid(self, form):
		#print(self)
		#print(form)
		#f = AuthorForm(request.POST)
        #self.object = form.save(commit=False)
        #self.object.course = self.course
        #self.object.save()

		#return HttpResponseRedirect(self.get_success_url())

	#def get_context_data(self, **kwargs):	
		#context = super(CmsCreateUser, self).get_context_data(**kwargs)
		#context["site_name"] = 	"ae"
		#context["title"] = 	"- Add User"
		#return context