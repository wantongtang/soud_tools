# coding =  utf-8
# the data preprocess of xiaoaitongxue as spotting
# author nifeng
# nifeng@qq.com




import  random
import string
import os


def get_name():
  ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
  return (ran_str.lower()+'_nohash_')



xatx_data_dir =  "../data/xatx"
dst_dir = '../data/xatx1'

for dir_name, _, filenames in os.walk(xatx_data_dir):
  k=0
  base_filename = get_name()
  for filename in filenames:
    src_filename = (os.path.join(dir_name,filename))
    dst_filename = (os.path.join(dst_dir,base_filename+str(k)+'.wav'))
    k+=1
    os.system("cp -rf %s %s"%(src_filename,dst_filename))
