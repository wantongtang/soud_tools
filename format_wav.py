# split a wav file into two wav file
# wtt
from pydub import AudioSegment
import os

import sys


def format_wav(filename):
  song =AudioSegment.from_wav(filename)
  song = song.set_sample_width(2)
  song = song.set_channels(1)
  song.export(filename,format='wav')  
   

if __name__=="__main__":
  if len(sys.argv) != 2:
    print("usage: python format_wav.py base_dir  ")  
    sys.exit()
  else:
    base_dir = sys.argv[1]
    for path,pathname,filenames in os.walk(base_dir):
      for filename in filenames:
        if filename.endswith('wav'):
          format_wav(os.path.join(path,filename))
