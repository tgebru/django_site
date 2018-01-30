from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from streetview.models import Synsets 

urlpatterns = patterns('',
    url(r'^$','cvpr2017.views.index'),
    url(r'([0-9]+)','cvpr2017.views.show_ims'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
