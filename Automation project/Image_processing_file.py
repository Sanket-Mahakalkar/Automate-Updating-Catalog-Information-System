#!/usr/bin/env python3
from PIL import Image
import os

#Processing images send by the supplier
user=os.getenv('USER') #To get the username from the environment
path='/home/{}/supplier-data/images/'.format(user)
for image in os.listdir(path):
  image_path=path+image
  mod_im=os.path.splitext(image_path)[0]
  mod_file = mod_im + '.jpeg'
  try:
    with Image.open(image_path).convert('RGB') as im:
      im.resize((600,400)).save(mod_file)
  except OSError:
    print('pass')
