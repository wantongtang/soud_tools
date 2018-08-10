# read wav and convert to standard wav

import os 
from pydub import AudioSegment

if __name__ == "__main__":
  
 filename  = './test.wav'
 sound = AudioSegment.from_file(filename,format='wav')
 sound = sound.set_sample_width(2)
 print(sound.sample_width) 
