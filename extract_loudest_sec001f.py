# extract the loudest section time  = 1400 ms

import os
import librosa
import sys
#def extract_loudest(filename):
#  for

def get_duration(filename):
  y, sr = librosa.load(filename,sr=16000)
  return librosa.get_duration(y,sr=sr)



if __name__ == "__main__":
  base_dir = sys.argv[1]  #'./xatx_qq_1_out_shaixuan_rename_format_converted'
  print("usage: python extract_loudest_sec.py src_dir ")
  for path,pathname,filenames in os.walk(base_dir):
    for filename in filenames:
      if filename.endswith('.wav'):
        if 1:# get_duration(os.path.join(path,filename)) >1.5:
          os.system('./extract_loudest_sec001f %s %s'%(os.path.join(path,filename),path ))
          print(filename)
        else:
          print("passed")
