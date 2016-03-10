from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile

class ProfileRegisterForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile        
        fields = ['name', 'email', 'password', 'password2', 'nui_id', 'staff', 'native', 'learning']


   # #def save(self, commit=True):
        # do something with self.cleaned_data['password']
        ##user = User.objects.create_user(self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['password'])
        ##user.save()
        #self.cleaned_data['user_id'] = 
        #print(self.cleaned_data) 

        #print(self.cleaned_data)
        #f = self(request.POST)
        ##profile = super(ProfileRegisterForm, self).save(commit=False)
        ##profile.user_id = user.id
        
        #for item in self.cleaned_data['learning']:
        	#profile.learning.add(item)
        ##commit = True
        ##if commit:       
        	##print("aqui") 	        	
        	##profile.save()
        	#print(profile.learning)
        	#f.save_m2m()

        ##return profile
        
        