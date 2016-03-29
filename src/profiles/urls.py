
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [   
	url(r'^register/$', ProfileRegister.as_view(), name='register'),
	url(r'^(?P<pk>\d+)/$', login_required(ProfileDetailView.as_view()), name='view'),
    url(r'^update/(?P<pk>\d+)/$', login_required(ProfileUpdate.as_view()), name='update'),
    url(r'^findfriends/$', login_required(FindFriends.as_view()), name='findfriends'),
    url(r'^addfriend/(?P<pk>\d+)/$', login_required(AddFriend.as_view()), name='addfriend'),
    url(r'^acceptfriend/(?P<pk>\d+)/$', login_required(AcceptFriendship.as_view()), name='acceptfriend'),    
]
