from django import forms
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
import re
import io
from PIL import Image

class ProfileRegisterForm (forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Profile        
        fields = ['username', 'email', 'password', 'password2', 'name', 'picture', 'nui_id', 'staff', 'native', 'learning', 'about']
        widgets={
                "name":forms.TextInput(attrs={'class':'form-control'}),
                "email":forms.EmailInput(attrs={'class':'form-control'}),  
                "nui_id":forms.TextInput(attrs={'class':'form-control'}),
                "about":forms.Textarea(attrs={'class':'form-control materialize-textarea'}),
                } 
        
    def __init__(self, *args, **kwargs):
        super(ProfileRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Full Name"
        self.fields['password2'].label = "Repeat Password"
        self.fields['nui_id'].label = "NUI ID"
        self.fields['staff'].label = "Are you Staff Member?"
        self.fields['native'].label = "Native Language"
        self.fields['learning'].label = "Language(s) I want to learn"
        self.fields['about'].label = "About me"


    def clean(self):
        cleaned_data = super(ProfileRegisterForm, self).clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match"
            )


    def clean_email(self):       
        #cleaned_data = super(ProfileRegisterForm, self).clean()
        #email = cleaned_data.get("email")
        email = self.cleaned_data['email']
        test_email = re.search("@[\w.]+", email)
        if test_email.group() != "@nuigalway.ie":
            raise forms.ValidationError("You must use your NUI Galway email to sing in")
        else:
            return email

    def clean_username(self):
        #cleaned_data = super(ProfileRegisterForm, self).clean()
        #username = cleaned_data.get("username")
        username = self.cleaned_data['username']
        if (' ' in username):
            raise forms.ValidationError("Spaces not allowed for username")  
        else:
            return username


    def clean_picture(self):
        #print("TESTE")
        #print(self.cleaned_data.get('picture'))
        if(self.cleaned_data.get('picture')):
            image_field = self.cleaned_data.get('picture')
            image_file = io.BytesIO(image_field.read())
            image = Image.open(image_file)
            width, height = image.size

            #"Max width and height 800"        
            if (800.0 / width < 800.0 / height):
                factor = 800 / width
            else:
                factor = 800 / height

            new_w = int(width * factor)
            new_h = int(height * factor)

            image = image.resize((new_w, new_h), Image.ANTIALIAS)

            image_file = io.BytesIO()
            image.save(image_file, 'JPEG', quality=90)

            image_field.file = image_file

            return self.cleaned_data.get('picture')


        #image = Image.open(self.picture)
        #(width, height) = image.size

        

        #size = ( width / factor, height / factor)
        #image.resize(size, Image.ANTIALIAS)
        #image.save(self.photo.path)


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
        
        