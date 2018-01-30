import os
import sys
import pickle
import mysql.connector

cnx = mysql.connector.connect(host="imagenet",port=3306,user="tgebru",passwd="",db="geo")
cursor=cnx.cursor()

file_dir='/afs/cs.stanford.edu/u/tgebru/cars/streetview_labeling/mysite/car_dataset'
makes=open(os.path.join(file_dir,'makes.txt'),'rb').readlines()
makes=[m.decode('utf-8').strip() for m in makes]
make_model_dict=dict(zip(makes,[[]]*len(makes)))

for make_ind,make in enumerate(makes):
  print('processing %s %d out of %d'%(make,make_ind,len(makes)))
  sql_s='select distinct(model) from geocars.synsets'
  cursor.execute(sql_s)
  models=cursor.fetchall()
  make_model_dict[make]=[m[0].replace(' ','-') for m in models]
#print(make_model_dict)
pickle.dump(make_model_dict,open(os.path.join(file_dir,'make_model_dict.p'),'wb'),protocol=2)



