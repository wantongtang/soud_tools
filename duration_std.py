from pydub import AudioSegment
import os
import sys


def duration_std(src_file,dst_file):
  sound = AudioSegment.from_file(src_file)
  if len(sound) <1500:
    left = (1500 - len(sound) ) / 2
    silence = AudioSegment.silent(duration=left)
    sound = silence+sound+silence
    sound.export(dst_file,format='wav')
    
  print(len(sound))


if __name__ =="__main__" :
  if len(sys.argv) == 2:
    src_dir = sys.argv[1]
    dst_dir = src_dir
  elif len(sys.argv) == 3:
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]
  else:
    print("usage:\n python duration_std.py src_dir dst_dir  \n or   python duration_std.py src_dir \n ")
    sys.exit()

  for path,pathname,filenames in os.walk(src_dir):
    for filename  in filenames:
      print(filename)
      duration_std(os.path.join(path,filename),os.path.join(dst_dir,filename))


  print(src_dir)
  print(dst_dir)



