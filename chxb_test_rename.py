#
import os
from xatx_data_preprocess import get_name

base_dir = '../test_data/chxb/'
des_dir = '../test_data/chxb1'
for pathname,path,filenames in os.walk(base_dir):
  person_name = get_name()
  k = 0
  for filename in filenames:
    if filename.endswith('wav'):
    
      os.system('cp -rf  %s  %s'%((os.path.join(pathname,filename)),(os.path.join(des_dir,person_name+str(k)+'.wav'))))
      k+=1

