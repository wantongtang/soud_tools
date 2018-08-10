# extract the loudest section time  = 1400 ms

import os


#def extract_loudest(filename):
#  for


if __name__ == "__main__":
  base_dir = '../mydata/chxb'

  for path,pathname,filenames in os.walk(base_dir):
    for filename in filenames:
      print('./extract_loudest_sec %s %s'%(os.path.join(path,filename),path ))
