# coding=utf-8
# auther wtt
# remove unuseful file in chxb
import os



base_dir = '../../chxb/all/'



def check_contain_chinese(check_str):
  for ch in check_str.decode('utf-8'):
    if u'\u4e00' <= ch <= u'\u9fff':
      return True

  return False

for pathnames,path,filenames in  os.walk(base_dir):
  for filename in filenames:
#    print(filename)
    if not check_contain_chinese(filename):  
      print(filename)
    
'''
#      print(os.path.join(pathnames,filename))
      if not filename.endswith('wav'): 
        os.system('rm %s'%(os.path.join(pathnames,filename)))
'''
