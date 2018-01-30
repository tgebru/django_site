import pickle
import os

root_dir='/scail/data/group/vision/u/tgebru/caffe/timnit_data/cvpr2017_100/'

web_files=['train_web.txt', 'val_web.txt']#,'test_web.txt',
gsv_files=['train_gsv.txt', 'val_gsv.txt', 'test_gsv.txt']


train_web_dict={}
val_web_dict={}
test_web_dict={}
train_gsv_dict={}
val_gsv_dict={}
test_gsv_dict={}
web_dicts=[train_web_dict,val_web_dict]#,test_web_dict,
gsv_dicts=[train_gsv_dict,val_gsv_dict,test_gsv_dict]

class_to_group={}
c=0
lines=open('groups_100_labels.txt')
for l in lines:
  class_to_group[c]=int(l.split(',')[1].strip())
  c += 1

for f,d in zip(gsv_files+web_files,gsv_dicts+web_dicts):
  print 'processing %s'%f
  lines=open(os.path.join(root_dir,f),'rb').readlines()
  for l in lines:
    class_id=int(l.split(' ')[-1].strip())
    group_id=class_to_group[class_id]
    #group_id=l.split('\t')[-1].strip()
    if group_id in d:
      d[group_id].append(l)
    else:
      d[group_id]=[l]
  print d 
  pickle.dump(d,open(f.replace('txt','p'),'wb'))
  


  
