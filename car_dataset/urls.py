from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from streetview.models import Synsets 

urlpatterns = patterns('',
    url(r'^$','car_dataset.views.index'),
    url(r'([0-9]+)','car_dataset.views.show_ims'),
    url(r'([Aa-zZ0-9\-]+)','car_dataset.views.show_group_ids'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
