#
import os
from xatx_data_preprocess import get_name

base_dir = '../../chxb/all/'
des_dir = './temp/'
for pathname,path,filenames in os.walk(base_dir):
  person_name = get_name()
  k = 0
  for filename in filenames:
#    print(person_name+str(k))
    
#    print('cp -rf  %s  %s'%((os.path.join(pathname,filename)),(os.path.join(des_dir,person_name+str(k)+'.wav'))))
    os.system('cp -rf  %s  %s'%((os.path.join(pathname,filename)),(os.path.join(des_dir,person_name+str(k)+'.wav'))))
    #print(os.path.join(pathname,filename))
    k+=1

#    print('mv %s  %s')
