import os
import sys
import pickle
import mysql.connector

cnx = mysql.connector.connect(host="imagenet",port=3306,user="tgebru",passwd="",db="geo")
cursor=cnx.cursor()

file_dir='/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/car_dataset'
makes=open(os.path.join(file_dir,'makes.txt'),'rb').readlines()
makes=[m.decode('utf-8').strip() for m in makes]
make_group_dict=dict(zip(makes,[[]]*len(makes)))

for make_ind,make in enumerate(makes):
  print('processing %s %d out of %d'%(make,make_ind,len(makes)))
  sql_s='select distinct(group_id) from geocars.synsets'
  cursor.execute(sql_s)
  groups=cursor.fetchall()
  for group in groups:
    if not group[0]:
      continue
    group=group[0]
    sql_s='select model, min(year), max(year) from geocars.synsets where group_id=%d'%(group)
    cursor.execute(sql_s)
    info=cursor.fetchall()
    info_str='%s %s-%s'%(info[0][0],info[0][1],info[0][2])
    sql_s='select trim from geocars.synsets where group_id=%d'%(group)
    cursor.execute(sql_s)
    trims=cursor.fetchall()
    trims=list(set(trims))
    trim_info=','.join([ t[0] for t in trims])
    all_info=(group,info_str+' '+ trim_info)
    info_dict={}
    info_dict['group_id']=group
    info_dict['info']=all_info
    make_group_dict[make].append(info_dict)
print(make_group_dict)

pickle.dump(make_group_dict,open(os.path.join(file_dir,'make_group_dict.p'),'wb'))



