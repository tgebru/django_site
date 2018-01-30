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

file_dir='/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/cvpr2017'
groups_lines=open(os.path.join(file_dir,'groups_100_labels.txt'),'rb').readlines()

group_ids=[g.split(',')[1].strip() for g in groups_lines]

train_web_dict=pickle.load(open(os.path.join(file_dir, 'train_web.p'),'rb'))
val_web_dict=pickle.load(open(os.path.join(file_dir, 'val_web.p'),'rb'))
#test_web_dict=pickle.load(open(os.path.join(file_dir, 'test_web.p'),'rb'))

train_gsv_dict=pickle.load(open(os.path.join(file_dir, 'train_gsv.p'),'rb'))
val_gsv_dict=pickle.load(open(os.path.join(file_dir, 'val_gsv.p'),'rb'))
#test_gsv_dict=pickle.load(open(os.path.join(file_dir, 'test_gsv.p'),'rb'))

def index(request):
    return render_to_response('cvpr2017/index.html', {'group_ids':group_ids})

def show_ims(request, group_id):
  group_id=str(group_id)
  train_disp_web_dict=[]
  val_disp_web_dict=[]
  test_disp_web_dict=[]
  train_disp_gsv_dict=[]
  val_disp_gsv_dict=[]
  test_disp_gsv_dict=[]

  #Web ims
  #for dat,ddict,split in zip([train_web_dict, val_web_dict, test_web_dict],[train_disp_web_dict,val_disp_web_dict,test_disp_web_dict],['train','val','test']):
  for dat,ddict,split in zip([train_web_dict, val_web_dict],[train_disp_web_dict,val_disp_web_dict],['train','val']):
    #ims=dat[group_id]
    ims=dat[int(group_id)]
    for im_info in ims:
      im_dat=im_info.split('\t') 
      im={}
      bbox={}
      img={}
      #bbox['x1']=int(im_dat[2].strip())
      #bbox['y1']=int(im_dat[3].strip())
      #bbox['x2']=int(im_dat[4].strip())
      #bbox['y2']=int(im_dat[5].strip())
      #im['bbox']=bbox
      im['url']=path_to_url(im_dat[0].split(' ')[0].strip())
      ddict.append(im)

  #GSV ims
  #for dat,ddict,split in zip([train_gsv_dict, val_gsv_dict, test_gsv_dict],[train_disp_gsv_dict,val_disp_gsv_dict,test_disp_gsv_dict],['train','val','test']):
  for dat,ddict,split in zip([train_gsv_dict, val_gsv_dict],[train_disp_gsv_dict,val_disp_gsv_dict],['train','val']):
    ims=dat[int(group_id)]
    for im_info in ims:
      im_dat=im_info.split('\t') 
      im={}
      bbox={}
      img={}
      #bbox['x1']=int(im_dat[2].strip())
      #bbox['y1']=int(im_dat[3].strip())
      #bbox['x2']=int(im_dat[4].strip())
      #bbox['y2']=int(im_dat[5].strip())
      #im['bbox']=bbox
      im['url']=path_to_url(im_dat[0].split(' ')[0].strip())
      ddict.append(im)

  web_ims=zip(['train','val','test'],[train_disp_web_dict,val_disp_web_dict,test_disp_web_dict])
  gsv_ims=zip(['train','val','test'],[train_disp_gsv_dict,val_disp_gsv_dict,test_disp_gsv_dict])
  im_sources=zip(['Web_Images','GSV_Images'],[web_ims,gsv_ims])

  return render_to_response('cvpr2017/show_ims.html',{'im_sources':im_sources})

def path_to_url(path):
 '''
 if '/imagenetdb/tgebru' in path:
   url=path.replace('/imagenetdb/tgebru/','imagenet.stanford.edu/internal/tgebru/') 
 elif 'imagenetdb2' in path:
   url=path.replace('/imagenetdb2/data/','imagenet.stanford.edu/internal/data/') 
 elif 'jkrause' in path:
   url=path.replace('/imagenetdb/jkrause/','imagenet.stanford.edu/internal/jkrause/jkrause/') 
 '''
 im_name=path.split('/')[-1]
 url='imagenet.stanford.edu/internal/scail_data/caffe/timnit_data/cvpr2017_100/images/'+im_name
 return url
