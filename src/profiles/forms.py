from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
import re

class ProfileRegisterForm (forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Repeat Password', 'class':'form-control'}))

    class Meta:
        model = Profile        
        fields = ['username', 'email', 'password', 'password2', 'name', 'nui_id', 'staff', 'native', 'learning']
        widgets={
                "name":forms.TextInput(attrs={'placeholder':'Full Name', 'class':'form-control'}),
                "email":forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'}),  
                "nui_id":forms.TextInput(attrs={'placeholder':'NUI ID', 'class':'form-control'}),
                "learning":forms.SelectMultiple(attrs={'class':'form-control'}),  
                } 
        
    def __init__(self, *args, **kwargs):
        super(ProfileRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Full Name"
        self.fields['password2'].label = "Repeat Password"
        self.fields['nui_id'].label = "NUI ID"
        self.fields['staff'].label = "Are you Staff Member?"
        self.fields['native'].label = "Native Language"
        self.fields['learning'].label = "Languages you want to learn"


    def clean(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match"
            )


    def clean_email(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        email = cleaned_data.get("email")
        test_email = re.search("@[\w.]+", email)
        if test_email.group() != "@nuigalway.ie":
            raise forms.ValidationError("You must use your NUI Galway email to sing in")
        else:
            return email
        



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
        
        