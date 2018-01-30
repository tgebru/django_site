import os
import sys

root_path = '/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling'
path = '/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite'
streetview_path = '/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/streetview'

if root_path not in sys.path:
    sys.path.append(root_path)
if path not in sys.path:
    sys.path.append(path)
if streetview_path not in sys.path:
    sys.path.append(streetview_path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
