from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from streetview.models import Synsets 

urlpatterns = patterns('',
    url(r'^$','timelapse.views.index'),
    url(r'siggraph_experiments/(.*)','timelapse.views.siggraph_experiments'),
    url(r'corr_scatter/(.*)/(.*)/(.*)','timelapse.views.corr_scatter'),
    url(r'predictions/(.*)/(.*)','timelapse.views.predictions_years'),
    url(r'corr_scatter/(.*)','timelapse.views.corr_scatter_years'),
    url(r'corr_plots/(.*)/(.*)','timelapse.views.corr_plots'),
    url(r'corr_plots/(.*)','timelapse.views.corr_plots_atts'),
    url(r'stats/','timelapse.views.get_stats'),
    url(r'NYC_diff_maps/','timelapse.views.get_nyc_diff_maps'),
    url(r'NYC_maps/','timelapse.views.get_nyc_maps'),
    url(r'all_maps/(.*)','timelapse.views.get_all_maps'),
    url(r'tgebru/','timelapse.views.tgebru'),
    url(r'correlations/(.*)/(.*)','timelapse.views.correlations_years'),
    url(r'car_atts/(.*)/(.*)','timelapse.views.car_atts'),
    url(r'housing/(.*)','timelapse.views.housing'),
    url(r'pascal_experiments/([0-9_\-\.]+)/([a-z]+)','timelapse.views.pascal_ims'),
    url(r'pascal_experiments/([0-9_\-\.]+)','timelapse.views.pascal_filter'),
    url(r'pascal_experiments/(.*)','timelapse.views.pascal_experiments'),
    url(r'city/siggraph/([0-9]+)','timelapse.views.show_siggraph_ims'),
    url(r'city/([a-z]+)','timelapse.views.city'),
    url(r'city/([0-9_\-\.]+)','timelapse.views.show_ims'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
