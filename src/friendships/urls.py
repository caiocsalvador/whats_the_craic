
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [   
	#url(r'^register/$', ProfileRegister.as_view(), name='register'),
	#url(r'^(?P<pk>\d+)/$', login_required(ProfileDetailView.as_view()), name='view'),
    #url(r'^update/(?P<pk>\d+)/$', login_required(ProfileUpdate.as_view()), name='update'), 
]
