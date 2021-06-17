#!/usr/bin/env python3
import os
import requests
import re

def file_system(file, image):
  #converting file content into dictionary format
  description={}
  try:
   with open(file) as f:
    i=0
    for line in f.readlines():
      if re.match(r"^[0-9]* [a-z]*?", line):
       result=re.search(r"^([0-9]*) [a-z]*?", line)
       description[keys[i]]=int(result.group(1))
       i+=1
      else:
       description[keys[i]]=line.strip()
       i+=1
  except IndexError:
    pass
  description['image_name']=image.strip('.txt')+ '.jpeg'
  return description



keys=['name', 'weight', 'description']
user=os.getenv('USER')
list=[]
path='/home/{}/supplier-data/'.format(user)
for image in os.listdir(path+'images/'):
  if re.match(r"^[0-9]*.jpeg", image):
    list.append(image)

for file in os.listdir(path+'descriptions/'):
  description_dict=file_system(path+'descriptions/'+file, file)
  #Sending description files on web server by converting file into json object
  response = requests.post('http://34.72.10.179/fruits/', json=description_dict)
  response.raise_for_status()
