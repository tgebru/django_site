import pickle
import os

web_root_dir='/scail/data/group/vision/u/tgebru/car_dataset/car_dataset/'
gsv_root_dir='/scail/data/group/vision/u/tgebru/science_submission/annotations/gsv_annos'

#Web files (containts, train,val,test slpits)
web_bbox_files='bboxes.txt'
web_files='car_big_splits.txt'

#Web bbox format like 
#train/00001/000020.jpg  24,83,567,265
#GSV format like
#im_30.382317_-81.656689_180.000000_0.000000.jpg

web_lines=open(os.path.join(web_root_dir,web_files),'r').readlines()
web_bbox_lines=open(os.path.join(web_root_dir,web_bbox_files),'r').readlines()

gsv_train_lines=open(os.path.join(gsv_root_dir,'gsv_train.txt'),'r').readlines()
gsv_val_lines=open(os.path.join(gsv_root_dir,'gsv_val.txt'),'r').readlines()
gsv_test_lines=open(os.path.join(gsv_root_dir,'gsv_test.txt'),'r').readlines()
gsv_lines=gsv_train_lines+gsv_val_lines+gsv_test_lines

web_dict={}
gsv_dict={}

#GSV
gsv_root='imagenet.stanford.edu/geo/gsv_100k_unwarp'
web_root='imagenet.stanford.edu/internal/scail_data/car_dataset/car_dataset'
for l in gsv_lines:
    splits=l.split(',')
    url=os.path.join(gsv_root,splits[0].strip())
    print(url)
    bbox=splits[1].strip()
    bbox_split=bbox.split(' ')
    group_id=splits[2].strip()
    bbox_dict={}
    bbox_dict['x1']=bbox_split[0].strip()
    bbox_dict['y1']=bbox_split[1].strip()
    bbox_dict['x2']=bbox_split[2].strip()
    bbox_dict['y2']=bbox_split[3].strip()
    image_dict={}
    if group_id not in gsv_dict:
      gsv_dict[group_id]={'images':[],'bboxes':[]}
    gsv_dict[group_id]['images'].append(url)
    gsv_dict[group_id]['bboxes'].append(bbox_dict)

#Web
for l,b in zip(web_lines,web_bbox_lines):
    splits=l.split('\t')
    group_id=splits[0].strip()
    url=b.split('\t')[0].strip()
    url=os.path.join(web_root,url)
    print(url)
    bbox=splits[3].strip()
    bbox_split=bbox.split(',')
    bbox_dict={}
    bbox_dict['x1']=bbox_split[0].strip()
    bbox_dict['y1']=bbox_split[1].strip()
    bbox_dict['x2']=bbox_split[2].strip()
    bbox_dict['y2']=bbox_split[3].strip()
    if group_id not in web_dict:
      web_dict[group_id]={'images':[],'bboxes':[]}
    web_dict[group_id]['images'].append(url)
    web_dict[group_id]['bboxes'].append(bbox_dict)


#Save dicts
pickle.dump(web_dict,open('web_dict.p','wb'),protocol=2)
pickle.dump(gsv_dict,open('gsv_dict.p','wb'),protocol=2)
  
