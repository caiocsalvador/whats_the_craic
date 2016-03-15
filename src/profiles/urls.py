
from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [   
	url(r'^register/$', ProfileRegister.as_view(), name='register'),
	url(r'^(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='view'),
    url(r'^update/(?P<pk>\d+)/$', ProfileUpdate.as_view(), name='update'),
    #url(r'^$', ProductListView.as_view(), name='list'),
    #url(r'^add/$', ProductCreateView.as_view(), name='crete'),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    #url(r'^(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='detail_slug'),
    #url(r'^(?P<pk>\d+)/download/$', ProductDownloadView.as_view(), name='download'),
    #url(r'^(?P<slug>[\w-]+)/download/$', ProductDownloadView.as_view(), name='download_slug'),
    #url(r'^(?P<pk>\d+)/edit/$', ProductUpdateView.as_view(), name='update'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', ProductUpdateView.as_view(), name='update_slug'),#
]
