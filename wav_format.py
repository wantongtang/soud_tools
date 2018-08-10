# read wav and convert to standard wav

import os 
from pydub import AudioSegment

if __name__ == "__main__":
  
  base_dir = '../mydata/chxb'
  
  for path,pathname,filenames in os.walk(base_dir):
    for filename in filenames:
      sound = AudioSegment.from_file(os.path.join(path,filename),format = 'wav')
      if sound.sample_width != 2:
        print(filename)
        print(sound.sample_width)
        sound = sound.set_sample_width(int(2))
        sound.export(os.path.join(path,filename),format = 'wav')
#      print(filename) 
