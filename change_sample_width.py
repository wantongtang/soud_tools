
from pydub import AudioSegment

import os



def change_sample_width(filename, dst_width=2,out_format = 'wav'):
  sound = AudioSegment.from_file(filename, format = out_format)
  if sound.sample_width != 2:
    sound = sound.set_sample_width(dst_width)
    sound.export(filename, format=out_format)
    print("canged sample_width")
  else:
    print("sample_width not changed")

if __name__ == "__main__":
  #base_dir = "../mydata1"
  base_dir = sys.argv[1]#"../mydata1"
  for path,pathname, filenames in os.walk(base_dir):
    for filename in filenames:
      print(filename)
      change_sample_width(os.path.join(path,filename),dst_width=2,out_format = 'wav')
  
