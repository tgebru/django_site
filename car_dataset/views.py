from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
import re
import sys
import os
import pickle

file_dir='/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/car_dataset'
groups_lines=open(os.path.join(file_dir,'groups_100_labels.txt'),'rb').readlines()
makes=open(os.path.join(file_dir,'makes.txt'),'rb').readlines()
group_ids=[g.split(',')[1].strip() for g in groups_lines]
model_group_dict=pickle.load(open(os.path.join(file_dir,'model_group_dict.p'), 'rb'))
make_model_dict=pickle.load(open(os.path.join(file_dir,'make_model_dict.p'), 'rb'))


#Image URLs
#train_web_dict=pickle.load(open(os.path.join(file_dir, 'train_web.p'),'rb'))
#val_web_dict=pickle.load(open(os.path.join(file_dir, 'val_web.p'),'rb'))
#test_web_dict=pickle.load(open(os.path.join(file_dir, 'test_web.p'),'rb'))

#train_gsv_dict=pickle.load(open(os.path.join(file_dir, 'train_gsv.p'),'rb'))
#val_gsv_dict=pickle.load(open(os.path.join(file_dir, 'val_gsv.p'),'rb'))
#test_gsv_dict=pickle.load(open(os.path.join(file_dir, 'test_gsv.p'),'rb'))

#Image dictss
web_dict=pickle.load(open(os.path.join(file_dir,'web_dict.p'),'rb'))
gsv_dict=pickle.load(open(os.path.join(file_dir,'gsv_dict.p'),'rb'))

def index(request):
    return render_to_response('car_dataset/index.html', {'makes':makes})

def show_models(request,make):
    models=make_model_dict[make]
    return render_to_response('car_dataset/show_models.html', {'models':models})

def show_group_ids(request, model):
    models=''
    if model.startswith('make'):
      make=model.split('-')[1]
      models=make_model_dict[make]
      return render_to_response('car_dataset/show_models.html', {'models':models})
    
    groups=model_group_dict[model]
    return render_to_response('car_dataset/show_groups.html', {'groups':groups})
    
def show_ims(request, group_id):
  group_id=str(group_id)
  web_ims=zip(web_dict[group_id]['images'], web_dict[group_id]['bboxes'])
  gsv_ims=zip(gsv_dict[group_id]['images'], gsv_dict[group_id]['bboxes'])

  im_sources=zip(['Web Images','GSV Images'],[web_ims,gsv_ims])
  return render_to_response('car_dataset/show_ims.html',{'im_dicts':im_sources})

