from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^polls/', include('polls.urls')),
  url(r'^streetview/', include('streetview.urls')),
  url(r'^timelapse/', include('timelapse.urls')),
  url(r'^cvpr2017/', include('cvpr2017.urls')),
  url(r'^car_dataset/', include('car_dataset.urls')),
  url(r'^admin/', include(admin.site.urls)),
)

