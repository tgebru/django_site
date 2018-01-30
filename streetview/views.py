from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from streetview.models import Synsets  
from streetview.models import GroupNames
from streetview.models import EdmundExamples
from streetview.models import PositiveExamples
from streetview.models import Bboxes
from streetview.models import Cur_state
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from datetime import timedelta
from datetime import datetime
from django.db.models import Count
import re
import sys
import unicodedata
sys.path.append('/imagenetdb/tgebru/') 
from mysql_utils import connect_to_db

date_threshold=timedelta(hours=3)

def get_images_for_group(group_id,cursor):
  #Get positive examples for selected images
  sql_s='select distinct(path),viewpoint from edmund_examples,positive_examples where edmund_examples.group_id=%d and edmund_examples.group_id=positive_examples.group_id and path not like "%%flipped%%" order by rand()'%(group_id)
  cursor.execute(sql_s)
  paths=cursor.fetchall()
  real_paths=get_images(paths)
  return real_paths

def get_im_bbox(b):
  db = connect_to_db('bbox_collection_gsv') 
  cursor = db.cursor()
  img_query='select myori_url,oriwidth,oriheight from imagenet_bbox.view_allimage where synsetid=%d and imageid=%d'%(b.bbox.synsetid, b.bbox.imageid) 
  cursor.execute(img_query)
  row=cursor.fetchone()

  bbox_query='select pleft, pright, ptop, pbottom, width, height from bbox_answer where bbox_isgood and pleft!=-1 and synsetid=%s and targetsynsetid=%s and imageid=%d and assignid=%d'%(b.bbox.synsetid,b.bbox.synsetid,b.bbox.imageid,b.bbox.assignid)
    
  cursor.execute(bbox_query) 
  bbrow=cursor.fetchone()
  bbox={}
  bbox['bbox_id']=b.bbox.bbox_id
  bbox['pleft']=bbrow[0]
  bbox['pright']=bbrow[1]
  bbox['ptop']=bbrow[2]
  bbox['pbottom']=bbrow[3]
  bbox['width']=bbrow[4]
  bbox['height']=bbrow[5]
  img={}
  img['url']=row[0]
  img['oriwidth']=row[1]
  img['oriheight']=row[2]
    
  db.close()
  return img,bbox

def submodel_only_matches(request,usr):
  if usr is None or usr=='' or usr=='/':
    total_ims=Bboxes.objects.filter(group_id= None).exclude(make=None).exclude(submodel='unknown').exclude(submodel=None).filter(make='unknown').filter(cur_state__box_done=1).values('make','submodel').annotate(Count('make'),Count('submodel'))
  else:
    total_ims=Bboxes.objects.filter(cur_state__user=usr).filter(group_id= None).exclude(make=None).exclude(submodel='unknown').exclude(submodel=None).filter(make='unknown').filter(cur_state__box_done=1).values('make','submodel').annotate(Count('make'),Count('submodel'))

  return render_to_response('streetview/make_submodel_matches.html',{'total_ims':total_ims,'username':usr})

def make_only_matches(request,usr):
  if usr is None or usr=='' or usr=='/':
    total_ims=Bboxes.objects.filter(group_id= None).exclude(make=None).filter(submodel='unknown').exclude(submodel=None).exclude(make='unknown').filter(cur_state__box_done=1).values('make','submodel').annotate(Count('make'),Count('submodel'))
  else:
    total_ims=Bboxes.objects.filter(cur_state__user=usr).filter(group_id= None).exclude(make=None).filter(submodel='unknown').exclude(submodel=None).exclude(make='unknown').filter(cur_state__box_done=1).values('make','submodel').annotate(Count('make'),Count('submodel'))

  return render_to_response('streetview/make_submodel_matches.html',{'total_ims':total_ims,'username':usr})

def make_submodel_matches(request,usr):
  if usr is None or usr=='' or usr=='/':
    total_ims=Bboxes.objects.filter(group_id= None).exclude(make=None).exclude(submodel='unknown').exclude(submodel=None).exclude(make='unknown').values('make','submodel').filter(cur_state__box_done=1).annotate(Count('make'),Count('submodel'))
  else:
    total_ims=Bboxes.objects.filter(group_id= None).exclude(make=None).exclude(submodel='unknown').exclude(submodel=None).exclude(make='unknown').values('make','submodel').filter(cur_state__user=usr).filter(cur_state__box_done=1).annotate(Count('make'),Count('submodel'))
  
  return render_to_response('streetview/make_submodel_matches.html',{'total_ims':total_ims,'username':usr})
  
def make_submodel_match(request,make_model,usr):
  make=make_model.split('-')[0]
  submodel=make_model.split('-')[1]
  ims=[]

  if usr is None or usr=='' or usr=='/':
    bbox_ids=Bboxes.objects.filter(make=make).filter(submodel=submodel).filter(cur_state__box_done=1).filter(group_id=None).values('bbox_id') 
  else:
    bbox_ids=Bboxes.objects.filter(cur_state__user=usr).filter(make=make).filter(submodel=submodel).filter(cur_state__box_done=1).filter(group_id=None).values('bbox_id') 

  for box in bbox_ids: 
    b=Cur_state.objects.filter(bbox_id=box['bbox_id']).get()
    img,bbox=get_im_bbox(b)
    im ={}
    im['img']=img
    im['bbox']=bbox
    ims.append(im)

  return render_to_response('streetview/show_make_submodel.html',{'images':ims,'make':make,'submodel':submodel,'username':usr})

def exact_match(request,g_id,usr):
  if usr is None or usr=='' or usr=='/':
    bbox_ids=Bboxes.objects.filter(group_id=g_id).filter(cur_state__box_done=1).values('bbox_id')
  else:
    bbox_ids=Bboxes.objects.filter(group_id=g_id).filter(cur_state__box_done=1).filter(cur_state__user=usr).values('bbox_id')
  ims=[]
  for box in bbox_ids: 
    b=Cur_state.objects.filter(bbox_id=box['bbox_id']).get()
    img,bbox=get_im_bbox(b) 
    im ={}
    im['img']=img
    im['bbox']=bbox
    ims.append(im)
       
  db = connect_to_db('backup_geocars')
  cursor = db.cursor()
  examples=get_images_for_group(int(g_id.encode('ascii','ignore')),cursor)
  db.close()
  group_name=GroupNames.objects.filter(group_id=g_id).values('group_name').get()

  return render_to_response('streetview/show_exact.html',{'images':ims,'examples':examples,'group_name':group_name,'group_id':g_id,'username':usr})
   
def exact_matches(request,usr):
  e_matches=[]
  if usr is None or usr=='' or usr=='/':
    exact_matches=Bboxes.objects.exclude(group_id= None).values('group_id').annotate(mcount=Count('group_id'))
    #exact_matches=Bboxes.objects.exclude(group_id= None).values('group_id').annotate(mcount=Count('group_id'))
  else:
    exact_matches=Bboxes.objects.exclude(group_id= None).values('group_id').filter(cur_state__user=usr).annotate(mcount=Count('group_id'))
  
  for m in exact_matches:
    group={}
    group_name=GroupNames.objects.filter(group_id= m['group_id']).values('group_name').get()
    group['group_id']=m['group_id']
    group['group_name']=group_name
    group['count']=m['mcount']
    e_matches.append(group)
  
  return render_to_response('streetview/exact.html', {'matches':e_matches,'username':usr})
  
def worker_results(request):
  people=[]
  users=Cur_state.objects.values('user').distinct()
  num_users=len(users)
  i=0;
  for usr in users:
    worker={}
    worker['name']=usr['user']
    worker['total_ims']=Cur_state.objects.filter(user=usr['user']).filter(box_done=1).count()
    worker['exact_matches']=Cur_state.objects.filter(user=usr['user']).filter(box_done=1).exclude(bbox__group_id=None).count()
    #worker['ave_speed']=
    people.append(worker)
    
  return render_to_response('streetview/worker_results.html',{'workers':people})
   
def summary(request,usr):
  show_worker=False
  if usr is None or usr=='':
    total_ims=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).all().count()
    exact_matches=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).exclude(bbox__group_id=None).count()
    make_only_matches=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).filter(bbox__group_id=None).exclude(bbox__make='unknown').filter(bbox__submodel='unknown').count()
    submodel_only_matches=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).filter(bbox__group_id=None).filter(bbox__make='unknown').exclude(bbox__submodel='unknown').exclude(bbox__submodel=None).count()
    make_submodel_matches=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).filter(bbox__group_id= None).exclude(bbox__make=None).exclude(bbox__submodel='unknown').exclude(bbox__submodel=None).exclude(bbox__make='unknown').count()
    unknown=Cur_state.objects.filter(ground_truth=0).filter(box_done=1).filter(bbox__submodel='unknown').filter(bbox__make='unknown').filter(bbox__group_id=None).count()
    show_worker=True
  
  else:
    total_ims=Cur_state.objects.filter(box_done=1).filter(user=usr).count()
    exact_matches=Cur_state.objects.filter(box_done=1).exclude(bbox__group_id=None).filter(user=usr).count()
    make_only_matches=Cur_state.objects.filter(box_done=1).filter(bbox__group_id=None).exclude(bbox__make='unknown').filter(bbox__submodel='unknown').filter(user=usr).count()
    submodel_only_matches=Cur_state.objects.filter(box_done=1).filter(bbox__group_id=None).filter(bbox__make='unknown').exclude(bbox__submodel='unknown').exclude(bbox__submodel=None).filter(user=usr).count()
    make_submodel_matches=Cur_state.objects.filter(box_done=1).filter(bbox__group_id= None).exclude(bbox__make=None).exclude(bbox__submodel='unknown').exclude(bbox__submodel=None).exclude(bbox__make='unknown').filter(user=usr).count()
    unknown=Cur_state.objects.filter(box_done=1).filter(bbox__submodel='unknown').filter(bbox__make='unknown').filter(bbox__group_id=None).filter(user=usr).count()
    show_worker=False

  return render_to_response('streetview/summary.html', {'total_ims':total_ims,'exact_matches':exact_matches,'make_submodel_matches':make_submodel_matches,'make_only_matches':make_only_matches,'submodel_only_matches':submodel_only_matches,'unknown':unknown, 'show_worker':show_worker,'username':usr})

def get_next_image(username):
  global date_threshold
  now = timezone.now()
  try:
    if username.startswith('gtruth'):
      #b=Cur_state.objects.filter(bbox__new_big_enough=1).filter(bbox__big_enough=0).filter(box_selected=0)[:1].get()
      b=Cur_state.objects.filter(ground_truth=1).filter(box_selected=0)[:1].get()
      #b=Cur_state.objects.filter(box_selected=0).filter(bbox__big_enough=1)[:1].get()
    else:
      b=Cur_state.objects.filter(box_selected=0).filter(ground_truth=0).filter(bbox__big_enough=1)[:1].get()
    b.box_selected=True
    b.date_selected= now#datetime.now()
    b.save()
  except Cur_state.DoesNotExist:
    '''
    try:
      if not username.startswith('gtruth'):
        bboxes=Cur_state.objects.exclude(box_done=1).filter(box_selected=1).filter(bbox__big_enough=1).all()
        if bboxes:
          for b in bboxes:
            if datetime.now(b.date_selected.tzinfo)-b.date_selected<date_threshold:
              b.date_selected= now#datetime.now()
              b.save()
              break
        else:
          return '',''
      else:
          return '',''
    except Cur_state.DoesNotExist:
      return '','' 
    '''
    return '','' 

  return get_im_bbox(b)

def unknown(request,bbid):
  #set image to done
  if request.session.get('done',None)==True:
    b=Cur_state.objects.filter(bbox_id=int(bbid)).get()
    b.box_done=True
    b.bbox.group_id=None
    b.bbox.make= request.session.get('make',None)
    b.bbox.submodel=request.session.get('submodel',None)
    b.bbox.save()
    b.user=request.user.username
    b.save()
    return HttpResponseRedirect("http://imagenet.stanford.edu/streetview/streetview/")
   
  return HttpResponseRedirect("http://imagenet.stanford.edu/streetview/streetview/unknown")

def index(request):
  make_model_dicts,img,bbox=get_next_images(request.user.username)
  if img:
    request.session['image']=img
    request.session['bbox']=bbox
    request.session['done']=False
    return render_to_response('streetview/index.html', {'make_model_dicts':make_model_dicts,'image':img,'bbox':bbox},context_instance=RequestContext(request))

  else:
    return render_to_response('streetview/no_more.html')

def logout_first(request):
    bbox=request.session.get('bbox',None)
    if bbox:
      bbid=bbox['bbox_id']
      b=Cur_state.objects.filter(bbox_id=bbid).get()
      b.box_selected=False
      b.save()
    return redirect('http://imagenet.stanford.edu/streetview/streetview/logout/')

def register(request):
  if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
          new_user = form.save()
          return HttpResponseRedirect("http://imagenet.stanford.edu/streetview/streetview/")
  else:
      form = UserCreationForm()
  return render(request, "streetview/register.html", {
      'form': form,
  })
   
def submit(request,group_id):
  bbox=request.session.get('bbox',None)
  bbid=bbox['bbox_id']
  b=Cur_state.objects.filter(bbox_id=bbid).get()
  b.box_done=True
  b.box_good=True
  b.bbox.group_id=int(group_id)
  b.bbox.save()
  b.user=request.user.username
  b.save()
  return HttpResponseRedirect("http://imagenet.stanford.edu/streetview/streetview/")

def get_next_images(username):
  img,bbox=get_next_image(username)
  make_model_dicts=[]
  make_model_dict= {}
  if bbox:
    query_set=Synsets.objects.values('make','model').distinct().exclude(ignore_group=1).order_by('make','model')
    for q in query_set:
      make=q['make']
      if make in make_model_dict:
        make_model_dict[make].append(q['model'])
      else:
        make_model_dict[make]=[q['model']]

    #worst way to do this but leaving it for now
    keys=sorted(make_model_dict, key=lambda key: key)
    for k in keys:
      new_dict = {}
      new_dict['make']=k
      new_dict['models']=make_model_dict[k]
      make_model_dicts.append(new_dict)

  return make_model_dicts,img,bbox

def make_template_dict(in_dict,key1,key2):
  dict_list=[]
  keys=sorted(in_dict, key=lambda key: key)
  for k in keys:
    new_dict = {}
    new_dict[key1]=k
    new_dict[key2]=in_dict[k]
    dict_list.append(new_dict)
  
  return dict_list

def get_submodels(make):
  if make=='unknown': #Get all submodels from Jon 
    db = connect_to_db('geocars_crawled')
    cursor = db.cursor()
    submodel_query='select distinct(submodel) from control_classes order by submodel'
  else:  
    make_r=make.replace('_',' ')
    #Get submodel's from Jon's improved table
    db = connect_to_db('geocars_crawled')
    cursor = db.cursor()
    submodel_query='select distinct(submodel) from control_classes where make="%s" order by submodel'%(make_r)

  cursor.execute(submodel_query) 
  submodels=cursor.fetchall()
  submodel_list=[]
  for s in submodels:
    submodel_list.append(s[0])
  return submodel_list

def submodels(request,make):
  img=request.session.get('image',None)
  bbox=request.session.get('bbox',None)
  submodels=get_submodels(make)
  request.session['done']=True    
  request.session['make']=make

  return render_to_response('streetview/submodels.html',{'submodels':submodels,'make':make,'image':img,'bbox':bbox})

def get_names(group_info,make,submodel):
  #group_info eg. honda accord sedan 1990_1993 trims: se, ex, lx  
  #p=re.compile('[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9].+' '|[0-9][0-9][0-9][0-9].+')
  p=re.compile('[0-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9] trims' '|[0-9][0-9][0-9][0-9] trims')
  trim_name= p.findall(group_info)[0]
  trim_name=group_info[group_info.find(trim_name):]
  trim_name=trim_name.replace('_',' ')
  model_name=group_info.replace('_',' ').replace(make,'').replace(submodel,'').replace(trim_name,'')
  return model_name,trim_name  

def get_symlink(p):
  path=p[p.find('edmunds_images/')+len('edmund_images/')+1:]
  return path
    
def is_good_viewpoint(viewpoint):
  good_viewpoints = set(['fq', 'rq', 'pdo', 's', 'fqn', 'fql', 'fqh','pr', 'fs', 'f', 'rst', 'r', 'prq']) 
  return viewpoint in good_viewpoints

def get_viewpoint (viewpoint):
  back = set(['rq', 'rst', 'r'])
  front= set(['fq', 'fqn', 'fs', 'fql', 'fl','f','fqh'])
  right_side=set(['pr','prq'])
  left_side=set(['s'])

  if viewpoint in back: return 'back'
  if viewpoint in front: return 'front'
  if viewpoint in left_side: return 'left'
  if viewpoint in right_side: return 'right'
 
def get_images(paths):
  #get 4 images with each view point (front,back,sides)
  num_ims=4
  bad_ims=[]
  extra_ims=[]
  needed_viewpoints=set(['front','back','left','right'])

  if len(paths)<=num_ims:
    real_paths=[get_symlink(p[0]) for p in paths]
  else:
    real_paths=[]
    for p in paths:
      if len(real_paths)==num_ims:
         return real_paths
      path =get_symlink(p[0])
      v=p[1]
      if is_good_viewpoint(v):
        view=get_viewpoint(v)
        if view in needed_viewpoints:
          real_paths.append(path)
          needed_viewpoints.remove(view) 
        else: extra_ims.append(path)
      else:
        bad_ims.append(path)

  real_paths=add_to_list(real_paths,extra_ims,num_ims)
  real_paths=add_to_list(real_paths,bad_ims,num_ims)
  
  return real_paths

def add_to_list(in_list,add_list,list_size):
  num_left_over=list_size-len(in_list)
  i=0
  while i<len(add_list) and len(in_list)<num_left_over:
    in_list.append(add_list[i])
    i+=1
  return in_list
  
def save_make_submodel(username,make,submodel,bbid):
    b=Cur_state.objects.filter(bbox_id=bbid).get()
    b.box_done=True
    b.bbox.group_id=None
    b.bbox.make=make
    b.bbox.submodel=submodel
    b.bbox.save()
    b.user=username
    b.save()
  
def models_trims(request,make,submodel):
  request.session['submodel']=submodel
  username=request.user.username
  if make=='unknown' or submodel=='unknown': 
    bbox_id=int(request.session.get('bbox',None)['bbox_id'])
    save_make_submodel(username,make,submodel,bbox_id)
    return HttpResponseRedirect("http://imagenet.stanford.edu/streetview/streetview/")
  else:
    num_images=4
    make  = make.replace('_',' ')
    submodel = submodel.replace('_',' ')
    db = connect_to_db('geocars_crawled')
    cursor = db.cursor()
    
    #get group names & ids of all groups in submodel 
    group_query='select group_name,group_id from control_classes where make="%s" and submodel="%s"'%(make,submodel)
    cursor.execute(group_query)
    group_info=cursor.fetchall()
    model_dict={}
    
    for g in group_info:
      #Get positive examples for selected images
      sql_s='select distinct(path),viewpoint from backup_geocars.edmund_examples,backup_geocars.positive_examples where backup_geocars.edmund_examples.group_id=%d and backup_geocars.edmund_examples.group_id=backup_geocars.positive_examples.group_id and path not like "%%flipped%%" order by rand()'%(g[1])
      cursor.execute(sql_s)
      paths=cursor.fetchall()
      real_paths=get_images(paths)
      group_dict={}
      model_name,trim_name=get_names(g[0],make,submodel)
      group_dict['images']=real_paths
      group_dict['group_id']=g[1]
      group_dict['trim_name']=trim_name

      if model_name in model_dict:
        model_dict[model_name].append(group_dict)
      else:
        model_dict[model_name]=[group_dict]
      
    models=make_template_dict(model_dict,'model_name','trims')

    img=request.session.get('image',None)
    bbox=request.session.get('bbox',None)
    db.close()
    return render_to_response('streetview/models_trims.html', {'models':models,'make':make,'submodel':submodel,'image':img,'bbox':bbox})
