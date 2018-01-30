import os
import sys
import pickle
import mysql.connector

cnx = mysql.connector.connect(host="imagenet",port=3306,user="tgebru",passwd="",db="geo")
cursor=cnx.cursor()

file_dir='/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/car_dataset'

sql_s='select distinct(model) from geocars.synsets'
cursor.execute(sql_s)
raw_models=cursor.fetchall()
models=[m[0].replace(' ','-') for m in raw_models]
model_group_dict=dict(zip(models,[[]]*len(models)))

for model_ind,model in enumerate(raw_models):
  model=model[0]
  print('processing %s %d out of %d'%(model,model_ind,len(raw_models)))
  sql_s='select distinct(group_id) from geocars.synsets where model="%s"'%model
  #print(sql_s)
  cursor.execute(sql_s)
  groups=cursor.fetchall()
  for group in groups:
    if not group[0]:
      continue
    group=group[0]
    sql_s='select min(year), max(year) from geocars.synsets where group_id=%d'%(group)
    cursor.execute(sql_s)
    info=cursor.fetchall()
    info_str='%s-%s'%(info[0][0],info[0][1])
    sql_s='select trim from geocars.synsets where group_id=%d'%(group)
    cursor.execute(sql_s)
    trims=cursor.fetchall()
    trims=list(set(trims))
    trim_info=','.join([ t[0] for t in trims])
    all_info=info_str+' '+ trim_info
    info_dict={}
    info_dict['group_id']=group
    info_dict['info']=all_info
    model_group_dict[model.replace(' ', '-')].append(info_dict)

pickle.dump(model_group_dict,open(os.path.join(file_dir,'model_group_dict.p'),'wb'),protocol=2)



