from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from streetview.models import Synsets 

urlpatterns = patterns('',
    url(r'^exact_match/([0-9]+)/(.*)','streetview.views.exact_match'),
    url(r'^logout_first/$','streetview.views.logout_first'), 
    url(r'^login/$', 'django.contrib.auth.views.login', {
      'template_name': 'streetview/login.html',
      'redirect_field_name': 'streetview.views.index'
    }),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {
      'template_name': 'streetview/logout.html',
    }),
    url(r'^submodel_only_matches/(.*)','streetview.views.submodel_only_matches'),
    url(r'^make_only_matches/(.*)','streetview.views.make_only_matches'),
    url(r'^exact_matches/(.*)','streetview.views.exact_matches'),
    url(r'^worker_results/$','streetview.views.worker_results'),
    url(r'^results/([a-zA-Z-_]+)/(.*)','streetview.views.make_submodel_match'),
    url(r'^make_submodel_matches/(.*)','streetview.views.make_submodel_matches'),
    url(r'^summary/(.*)','streetview.views.summary'),
    url(r'^register/$','streetview.views.register'),
    url(r'^$','streetview.views.index'),
    url(r'bbox_id/([0-9]+)','streetview.views.unknown'),
    url(r'submit/([0-9_\-]+)', 'streetview.views.submit'),
    url(r'([a-z\-_]+)/([a-zA-Z0-9_\-]+)', 'streetview.views.models_trims'),
    url(r'([a-z\-_]+)','streetview.views.submodels'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
