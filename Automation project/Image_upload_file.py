#!/usr/bin/env python3
import requests
import os
#This shows how a file can be uploaded using python requests module

url='http://localhost/upload/'
user=os.getenv('USER')
path='/home/{}/supplier-data/images/'.format(user)
for image in os.listdir(path):
  if '.jpeg' in image:
    with open(path+image, 'rb') as opened:
      response=requests.post(url, files={'file': opened})
