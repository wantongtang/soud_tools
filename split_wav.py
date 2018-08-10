# split a wav file into two wav file
# wtt
from pydub import AudioSegment
import os

import sys

def split_wav(path,filename,dst_dir):
  song =AudioSegment.from_wav(os.path.join(path,filename))
  middle = int(len(song)/2)
  song1 = song[:middle]
  song2 = song[-middle:]
  filename1 = filename.split('.wav')[0] +'1' +'.wav'
  filename2 = filename.split('.wav')[0] +'2' +'.wav'
  song1.export(os.path.join(dst_dir,filename1),format='wav')
  song2.export(os.path.join(dst_dir,filename2),format='wav')
  print(filename2)
  
   

if __name__=="__main__":
  if len(sys.argv) != 3:
    print("usage: python split_wav.py base_dir  dst_dir ")  
    sys.exit()
  else:
    base_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    for path,pathname,filenames in os.walk(base_dir):
      for filename in filenames:
        split_wav(path,filename,dst_dir) 
