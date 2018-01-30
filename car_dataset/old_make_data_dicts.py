import pickle

files=['web_train_100.txt', 'web_val_100.txt','web_test_100.txt',
'gsv_train_100.txt', 'gsv_val_100.txt', 'gsv_test_100.txt']

train_web_dict={}
val_web_dict={}
test_web_dict={}
train_gsv_dict={}
val_gsv_dict={}
test_gsv_dict={}
dicts=[train_web_dict,val_web_dict,test_web_dict,
train_gsv_dict,val_gsv_dict,test_gsv_dict]

for f,d in zip(files,dicts):
  print 'processing %s'%f
  lines=open(f,'rb').readlines()
  for l in lines:
    group_id=l.split('\t')[-1].strip()
    if group_id in d:
      d[group_id].append(l)
    else:
      d[group_id]=[l]
  print d 
  pickle.dump(d,open(f.replace('txt','p'),'wb'))
  


  
