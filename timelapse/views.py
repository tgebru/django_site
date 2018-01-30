from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import redirect
import sys
import os
sys.path.append('/imagenetdb/tgebru/') 
from mysql_utils import connect_to_db
from datetime import datetime
from sets import Set
import random
import pickle

#min_pop=1000
#min_cars=100
#min_pop=0
#min_cars=0
min_pop=5000
min_cars=500
#min_pop=10
#min_cars=10

def index(request):
    return render_to_response('timelapse/index.html', {})

def tgebru(request):
    return render_to_response('timelapse/tgebru.html', {})

def city(request,cityname):
  if cityname=='nyc':
    cityid=175
  elif cityname=='detroit':
    cityid=155
  else:
    cityid=None 

  #Get image names and number of dates for each image
  #Get lat_long list from a file to make sure timelapse ims are ok
  experiment=True 
  #experiment=False
  if cityid:
    ll_list=get_lat_lng_list(cityid,experiment,request)
    return render_to_response('timelapse/show_im_list.html', {'ll_list':ll_list})
  else:
    im_list = get_siggraph_list()
  return render_to_response('timelapse/show_siggraph_im_list.html', {'im_list':im_list})

def get_siggraph_list():
    data_dir = '/imagenetdb3/data/geo/siggraph_timelapse'
    aligned_ims=os.path.join(data_dir,'imageAlignedLD')
    unaligned_ims=os.path.join(data_dir,'imageLD')
    im_list={}
    im_list['aligned']=[d for d in os.listdir(aligned_ims) if os.path.isdir(os.path.join(aligned_ims,d))]
    im_list['unaligned']=[ d for d in os.listdir(unaligned_ims) if os.path.isdir(os.path.join(unaligned_ims,d))]
    return im_list

def get_lat_lng_list(cityid,exp,request):
   ll_list=[]

   if exp== True: #False:
     db = connect_to_db('geo')
     zip=10011
     cursor=db.cursor()
     cityid=175
     sqls='select lat,lng,count(distinct(im_date)) from fixed_timelapse_times where cityid=%d and downloaded=1 and small=0 and corrupt=0 group by lat,lng'%(cityid);
     #sqls='select distinct t.lat,t.lng, count(im_date) from geo.timelapse_times t, demo.latlong_fpis l where zipcode=%d and l.lat=t.lat and l.lng=t.lng group by lat,lng'%zip
     cursor.execute(sqls)
     lat_lng_date=cursor.fetchall()
     NUM_SAMPLES=1000
     lat_lng_date=random.sample(lat_lng_date,NUM_SAMPLES) 
     lld_dict={}
     for l in lat_lng_date:
       ll_dict={} #need dict to traverse in view
       ll_dict['gps']='%s_%s'%(str(l[0]),str(l[1]))
       ll_dict['numdates']=int(l[2])
       ll_list.append(ll_dict)
       sqls='select distinct(im_date) from fixed_timelapse_times where lat=%s and lng=%s'%(str(l[0]),str(l[1]))
       cursor.execute(sqls)
       dates=cursor.fetchone()
       lld_dict['%s_%s'%(str(l[0]),str(l[1]))]=[str(d) for d in dates]
     db.close()  
     request.session['lld_dict']=lld_dict
   else: #Different file for training/test vs all timelapse
     #f=open('/imagenetdb/tgebru/scrape/lat_lng_rot_url.txt','rb')

     #Validation set for 2013 housing data
     #f=open('/imagenetdb3/tgebru/cvpr2016/housing_data/train_test_split_2013/housing_2013_class_val.txt','rb')
     
     #Only loaded images
     #f=open('/afs/cs.stanford.edu/u/tgebru/cvpr2016/loaded_lat_lng_rot_url.txt', 'rb')
     NUM_SAMPLES=1000
     #lines=f.readlines()
     #lines=random.sample(lines,UM_SAMPLES)
     #f.close()
     lld_dict={}

     #Load lat,lng,dates dict
     with open('/afs/cs.stanford.edu/u/tgebru/cvpr2016/ipython_code/kings_lat_lng_date_dict.pickle','rb') as f:
        lat_lng_date_dict=pickle.load(f)

     '''
     for l in lines: 
       #uncomment for all timelapse
       parts=l.split('\t') 
       lat=parts[0].split('_')[0].strip()
       lng=parts[0].split('_')[1].strip()
       date=parts[-1].split('_')[-1][0:-5].strip()

       #Uncomment for 2013 housing data
       #lat=l.split('/')[-1].split('_')[0].strip()
       #lng=l.split('/')[-1].split('_')[1].strip()
       #date=l.split('/')[-1].split('_')[-1].split(' ')[0][0:-4].strip()
       
       #Different file for training/test vs all timelapse
       lat_lng='%s_%s'%(lat,lng) 
       if lat_lng in lld_dict.keys():
         lld_dict[lat_lng].append(date)
       else:
         lld_dict[lat_lng]=[date]
     '''
     #Now create a list to send to the view
     #for k in lld_dict.keys():
     keys=random.sample(lat_lng_date_dict.keys(),NUM_SAMPLES) 
     for k in keys:
       ll_dict={}
       ll_dict['gps']=k
       dates=list(set(lat_lng_date_dict[k].keys()))
       numdates=len(dates)
       ll_dict['numdates']=numdates
       lld_dict[k]=dates
       #Only want to see images with multiple years
       if numdates > 1:
         ll_list.append(ll_dict)
     request.session['lld_dict']=lld_dict 

   return ll_list


def pascal_filter(request,filter):
    return render_to_response('timelapse/pascal_filter.html', {'filter':filter})

def pascal_ims(request,filter,exp):
    im_web_dir='/internal/geo/pascal_experiments/%s/%s'%(filter,exp)
    im_dir='/imagenetdb3/tgebru/pascal_experiments/%s/%s'%(filter,exp)
    im_list = [os.path.join(im_web_dir,i) for i in os.listdir(im_dir) if i.endswith('png')]
    random.shuffle(im_list)
    #Show 100 random examples
    im_list=im_list[0:100]
    return render_to_response('timelapse/siggraph_experiments.html', {'im_list':im_list}) 

def pascal_experiments(request,filter=None,exp=None):
   exp_dir='/imagenetdb3/tgebru/pascal_experiments'
   name_list=os.listdir(exp_dir)
   return render_to_response('timelapse/pascal_experiments.html',{'name_list':name_list})


def corr_scatter(request,data_type,year,census_att):
  geo=data_type.split('_')[0]
  if data_type.endswith('diff'):
    man_only=data_type.split('_')[-2]
    scatter_dir_base='cor_diff_minpop_%d_mincars_%d_scatter_%s_manh_%s'%(min_pop,min_cars,geo,man_only)
  else: 
    man_only=data_type[-1]
    scatter_dir_base='cor_minpop_%d_mincars_%d_scatter_%s_manh_%s'%(min_pop,min_cars,geo,man_only)
  base_dir='/imagenetdb/www/home/internal'
  if not census_att:
     att_list=os.listdir(os.path.join(base_dir,scatter_dir_base,'%s'%year))
     return render_to_response('timelapse/show_cor_census_list.html',{'att_list':att_list,'data_type':data_type,'year':year}) 

  else:
    img_list=os.listdir(os.path.join(base_dir,scatter_dir_base,'%s'%year,'%s'%census_att))

    return render_to_response('timelapse/show_cor_scatter.html',{'img_list':img_list,'year':year,'man':man_only,'base_dir':os.path.join(scatter_dir_base,'%s'%(year),'%s'%census_att)})


def corr_scatter_years(request,data_type):
  geo=data_type.split('_')[0]
  if data_type.endswith('diff'):
    man_only=data_type.split('_')[-2]
    scatter_dir_base='cor_diff_minpop_%d_mincars_%d_scatter_%s_manh_%s'%(min_pop,min_cars,geo,man_only)
  else:
    man_only=data_type[-1]
    scatter_dir_base='cor_minpop_%d_mincars_%d_scatter_%s_manh_%s'%(min_pop,min_cars,geo,man_only)

  base_dir='/imagenetdb/www/home/internal'

  year_list=os.listdir(os.path.join(base_dir,scatter_dir_base))
  years=[y for y in year_list if not y.startswith('.')]

  return render_to_response('timelapse/show_cor_scatter_list.html',{'year_list':list(set(years)),'data_type':data_type}) 

def corr_plots_atts(request,data_type):
  geo=data_type.split('_')[0]
  if data_type.endswith('diff'):
    man_only=data_type.split('_')[-2]
    plot_dir_base='cor_diff_minpop_%d_mincars_%d_plots_%s_manh_%s'%(min_pop,min_cars,geo,man_only)
  elif data_type.endswith('atts'):
    plot_dir_base='/imagenetdb/www/home/internal/new_census_diff_plots_minpop_%d_mincars_%d_filter_1_max_0_%s'%(min_pop,min_cars,geo)
  else:
    man_only=data_type[-1]
    plot_dir_base='cor_minpop_%d_mincars_%d_plots_%s_manh_%s'%(min_pop,min_cars,geo,man_only)

  base_dir='/imagenetdb/www/home/internal'

  att_list=os.listdir(os.path.join(base_dir,plot_dir_base))
  atts=[a for a in att_list if not a.startswith('.')]

  return render_to_response('timelapse/show_cor_plot_list.html',{'att_list':atts,'data_type':data_type}) 

def corr_plots(request,data_type,att):
  geo=data_type.split('_')[0]
  if data_type.endswith('diff'):
    man_only=data_type.split('_')[-2]
    plot_dir_base='cor_diff_minpop_%d_mincars_%d_plots_%s_manh_%s'%(min_pop,min_cars,geo,man_only)
  elif data_type.endswith('atts'):
    plot_dir_base='new_census_diff_plots_minpop_%d_mincars_%d_filter_1_max_0_%s'%(min_pop,min_cars,geo)
  else:
    man_only=data_type[-1]
    plot_dir_base='cor_minpop_%d_mincars_%d_plots_%s_manh_%s'%(min_pop,min_cars,geo,man_only)

  base_dir='/imagenetdb/www/home/internal'

  file_dir=os.path.join(base_dir,plot_dir_base,att)
  img_list=os.listdir(file_dir)

  return render_to_response('timelapse/show_cor_scatter.html',{'img_list':img_list,'base_dir':os.path.join(plot_dir_base,att),'year':'2012'})

def predictions_years(request,whole,year):
  whole=whole.encode('ascii').strip()

  if whole=='1':
    #scatter_dir='scatter_3_17_16/whole-cnn'
    #scatter_dir='scatter_3_17_16/whole-cars'
    scatter_dir='scatter_3_17_16/whole-cars_cnn'
    #scatter_dir='scatter_3_17_16/whole-census_baseline'
  else:
    scatter_dir='scatter_3_17_16'
    
  #'scatter' #'scatter_whole' #'scatter_softmax' 
  if not year:
     year_list=os.listdir('/imagenetdb/www/home/internal/%s'%scatter_dir)
     years=[]

     #Format of dir=test_train-2011_test-2012
     #Format train_train_diff_ZIPCODE-2007_test-2008-2008_2009-5_5_prev_0_man_1_minpop_1000_mincars_100
     for y in year_list: 
       years.append(y[y.find('_')+1:])
     return render_to_response('timelapse/show_scatter_list.html',{'year_list':list(set(years))}) 

  if not year.startswith('train'):
    img_list_train=os.listdir('/imagenetdb/www/home/internal/%s/city_%s'%(scatter_dir,year))
    img_list_test=os.listdir('/imagenetdb/www/home/internal/%s/city_%s'%(scatter_dir,year))
    year_list=['city_%s'%year]*len(img_list_test)
    img_list=zip(img_list_train,img_list_test,year_list)
    show_baselines='no'

  else:
    img_list_train=os.listdir('/imagenetdb/www/home/internal/%s/train_%s'%(scatter_dir,year))
    img_list_test=os.listdir('/imagenetdb/www/home/internal/%s/test_%s'%(scatter_dir,year))
    year_list=[year]*len(img_list_test)
    img_list=zip(img_list_train,img_list_test,year_list)
    show_baselines='yes';
  base_url=os.path.join('http://imagenet.stanford.edu/internal/',scatter_dir)

  return render_to_response('timelapse/show_scatter.html',{'img_list':img_list,'base_url':base_url,'show_baselines':show_baselines})

def housing(request,data_type):
    att_dir='/imagenetdb/www/home/internal/housing_plots_%s'%data_type
    dir_name='housing_plots_%s'%data_type
    att_list=os.listdir(att_dir)
    att_ims=[l for l in att_list if l.endswith('png')]
    name_list=[os.path.split(f)[1][:-4] for f in att_ims]
    img_list=zip(att_ims,name_list)
    return render_to_response('timelapse/show_car_att_plots.html',{'img_list':img_list,'dir_name':dir_name})


def car_atts(request,att_type,data_type):
  #Data type choices are DISTRICT,ZIPCODE, etc...
  if att_type=='cars':
    att_dir='/imagenetdb/www/home/internal/new_car_atts_%s'%data_type
    dir_name='new_car_atts_%s'%data_type
  else:
    #/new_census_plots_minpop_1000_mincars_100_filter_1_max_0_DISTRICT
    att_dir='/imagenetdb/www/home/internal/new_census_plots_minpop_0_mincars_0_filter_1_max_0_%s'%(data_type)
    dir_name=att_dir.split('/')[-1]

  att_list=os.listdir(att_dir)
  att_ims=[l for l in att_list if l.endswith('png')]
  name_list=[os.path.split(f)[1][:-4] for f in att_ims]
  img_list=zip(att_ims,name_list)
  return render_to_response('timelapse/show_car_att_plots.html',{'img_list':img_list,'dir_name':dir_name})

def get_all_maps(request,att=None):
   maps_dir='/imagenetdb/www/home/internal/maps/streetview_maps_good'
   http_maps_dir='/maps/streetview_maps_good'
   if att:
     ims=os.listdir(os.path.join(maps_dir,att))
     img_list=[f for f in ims if f.endswith('png')]
     return render_to_response('timelapse/show_att_ims.html',{'img_list':img_list,'img_dir':os.path.join(http_maps_dir,att)})

   att_list=os.listdir(maps_dir)
   return render_to_response('timelapse/show_census_list.html',{'att_list':att_list})



def get_nyc_maps(request):
   maps_dir='/imagenetdb/www/home/internal/maps/nyc'
   ims=os.listdir(maps_dir)
   img_list=[f for f in ims if f.endswith('png')]
   return render_to_response('timelapse/show_att_ims.html',{'img_list':img_list,'img_dir':'%s/%s'%(maps_dir.split('/')[-2],maps_dir.split('/')[-1])})

def get_nyc_diff_maps(request):
   maps_dir='/imagenetdb/www/home/internal/maps/nyc_diff'
   ims=os.listdir(maps_dir)
   img_list=[f for f in ims if f.endswith('png')]
   return render_to_response('timelapse/show_att_ims.html',{'img_list':img_list,'img_dir':'%s/%s'%(maps_dir.split('/')[-2],maps_dir.split('/')[-1])})

def get_stats(request):
   stats_dir='/imagenetdb/www/home/internal/stats'
   ims=os.listdir(stats_dir)
   img_list=[f for f in ims if f.endswith('png')]
   return render_to_response('timelapse/show_att_ims.html',{'img_list':img_list,'img_dir':stats_dir.split('/')[-1]})


def correlations_years(request,data_type,year):
  if data_type=='ZIPCODE_WHOLE':
    corr_dir='/imagenetdb/www/home/internal/whole_corrs_new_ZIPCODE_ny_0'
  elif data_type=='ZIPCODE_WHOLE_NY':
    corr_dir='/imagenetdb/www/home/internal/whole_corrs_new_ZIPCODE_ny_1'
  elif data_type=='ZIPCODE_MAN':
    corr_dir='/imagenetdb/www/home/internal/corrs_new_ZIPCODE_manh_1'
  elif data_type=='DISTRICT_MAN':
    corr_dir='/imagenetdb/www/home/internal/corrs_new_DISTRICT_manh_1'
  else:
    corr_dir='/imagenetdb/www/home/internal/corrs_new_%s'%(data_type)
  if not year:
     year_list=os.listdir(corr_dir)
     years=[]
     #file name format
     #demo_corrs_2011.rc.0.minp.5000.minc.500_sorted.txt
     for y in year_list: 
       year_sub=y.split('.')[0]
       years.append(year_sub[year_sub.rfind('_')+1:])
     return render_to_response('timelapse/show_corr_list.html',{'year_list':list(set(years))}) 

  corr_file='demo_corrs_%s.rc.1.minp.%d.minc.%d_sorted.txt'%(year,min_pop,min_cars)
  lines=open(os.path.join(corr_dir,corr_file),'r').readlines()
  year_list=[year]*len(lines)
  corr_list=zip(lines,year_list)
  return render_to_response('timelapse/show_corrs.html',{'corr_list':corr_list})


def siggraph_experiments(request,exp):
   im_web_dir='/internal/geo/siggraph_experiments'
   im_dir='/imagenetdb3/tgebru/siggraph_experiments'
   im_list = [os.path.join(im_web_dir,i) for i in os.listdir(im_dir) if i.endswith('png')]
   return render_to_response('timelapse/siggraph_experiments.html', {'im_list':im_list}) 

def show_siggraph_ims(request,im_number):
   web_path_prefix='/internal/geo/siggraph_timelapse/imageAlignedLD/'
   path_prefix='/imagenetdb3/data/geo/siggraph_timelapse/imageAlignedLD/'
   im_web_dir=os.path.join(web_path_prefix,im_number)
   im_dir=os.path.join(path_prefix,im_number)
   ims = [os.path.join(im_web_dir,i) for i in os.listdir(im_dir) if i.endswith('jpg')]
   im_list=[]
   num_ims=len(ims)
   cur_num=0
   for i in ims:
     im={}
     im['im']=i
     cur_num += 1
     im['num']='%d out of %d'%(cur_num, num_ims)
     im_list.append(im)

   return render_to_response('timelapse/show_siggraph_ims.html',{'im_list':im_list})

def make_bbox_pred_dict(bbox_list):
  bboxes=[]
  for b in bbox_list:
    bbox={}
    bbox['x1']=b[0]
    bbox['y1']=b[1]
    bbox['x2']=b[2]
    bbox['y2']=b[3]
    bbox['dscore']=b[4]
    bbox['pscore']=b[5]
    bbox['group_id']=b[6]
    bboxes.append(bbox)

  return bboxes

def show_ims(request,lat_lng):
   #exp=True means experimenting to see if images are 
   #being downloaded properly
   exp=True 
   #exp=False
   dates_list=[]
   lat=lat_lng.split('_')[0].encode('ascii','ignore')
   lng=lat_lng.split('_')[1].encode('ascii','ignore')
   db=connect_to_db('geo') 
   cursor=db.cursor()
   if exp== True:#False:
      sqls='select distinct(im_date) from fixed_timelapse_times where lat=%s and lng=%s and small=0 and corrupt=0 and downloaded=1'%(lat,lng)
      cursor.execute(sqls)
      im_dates=cursor.fetchall() 
      for d in im_dates: 
        dates_list.append(d[0])
   else:
      lld_dict=request.session['lld_dict']
      for l in lld_dict[lat_lng]: 
        dates_list.append(l.encode('ascii','ignore'))
      dates_list=list(set(dates_list))
  
   dates_list.sort()
   dates_list_str=[datetime.strftime(d,"%Y-%b-%d") for d in dates_list]
   rots=[0,60,120,180,240,300]
   im_list=[]
   for r in rots:
     im_rot_list=[] 
     for d,d_str in zip(dates_list,dates_list_str):
        year=d_str.split('-')[0]
        month=d_str.split('-')[1]
        date_str='%s-%s-01'%(year,month)
        sqls='select corrupt,small,downloaded from geo.fixed_timelapse_times where lat=%s and lng=%s and rot=%s and im_date="%s"'%(lat,lng,r,datetime.strftime(d,"%Y-%m-%d"))
        cursor.execute(sqls)
        res=cursor.fetchone()
        if int(res[0])==0 and int(res[1])==0 and int(res[2])==1:
          im_dict={}
          im_name=lat_lng_to_path(lat,lng,r,'%s-%s'%(month,year))
          print im_name
          im_dict['im'] =im_name
          im_dict['date'] =d
          im_dict['rot'] =r
          sql_s='select x1,y1,x2,y2,desc_val,pscore,group_id from  all_cars.city_175_timelapse_detected_cars where lat=%s and lng=%s and rot=%s and im_date="%s"'%(lat,lng,r,datetime.strftime(d,"%Y-%m-%d"))
          cursor.execute(sql_s)
          bboxes_list=cursor.fetchall()
          bboxes=make_bbox_pred_dict(bboxes_list)
          im_dict['bboxes']=bboxes
          im_rot_list.append(im_dict)
     im_list.append(im_rot_list)
 
   return render_to_response('timelapse/show_ims.html',{'im_list':im_list})
    
def lat_lng_to_path(lat,lng,rot,date):
  '''Converts latitude and longitude into a folder to save images in.'''
  #base_dir = '/internal/geo/gsv_time_unwarp/'
  #unwarping takes out adress info so look at warped for now
  #base_dir = '/internal/geo/gsv_time/'
  base_dir = '/internal/geo/gsv_time_fixed_unwarp/'
  real_base_dir='/imagenetdb3/data/geo/gsv_time_fixed_unwarp/'
  lat_base = lat.split('.')[0]
  lng_base = lng.split('.')[0]
  subfolder1 = '%s_%s' % (lat_base, lng_base)
  lat_dec = lat.split('.')[1]
  lng_dec = lng.split('.')[1]
  subfolder2 = '%s_%s' % (lat_dec[0], lng_dec[0])
  subfolder3 = '%s_%s' % (lat_dec[1], lng_dec[1])
  subfolder4 = '%s_%s' % (lat_dec[2], lng_dec[2])
  pitch=0
  im_name = '%0.6f_%0.6f_%d_%s.jpg'%(float(lat), float(lng), rot,date)
  im_path=os.path.join(base_dir, subfolder1, subfolder2, subfolder3, subfolder4,im_name)
  if os.path.exists(im_path.replace(base_dir,real_base_dir)):
    return im_path
  else: 
    return im_path.replace('jpg','png')
