from pydub import AudioSegment
import os
import librosa
import sys


def half_wav(src_dir,dst_dir):
  for path,pathname,filenames in os.walk(src_dir):
    for filename in filenames:
      # create new_filename that are aparted
      new_filename1 = filename.split('.wav')[0]+'1'+'.wav'
      new_filename2 = filename.split('.wav')[0]+'2'+'.wav'
      
      sound = AudioSegment.from_file(os.path.join(path,filename), format="wav")
      leng = int( len(sound)/2)
      sound1 = sound[:leng]
      sound2 = sound[-leng:]
      sound1.set_sample_width(2)
      sound2.set_sample_width(2)
      sound1.set_channels(1)
      sound2.set_channels(1)
      
      sound1.export(os.path.join(dst_dir,new_filename1),format='wav')
      sound2.export(os.path.join(dst_dir,new_filename2),format='wav')
  
      
  

if __name__ == "__main__":
  
  if len(sys.argv) != 3:
    print("usage: python half_wav.py src_dir dst_dir")
  else:
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
    half_wav(src_dir,dst_dir) 

