# coding = utf-8
# author wtt
import os
import librosa
import numpy as np
from pydub import AudioSegment


# read a file, change its sample_width to dst_width and save it as the same name
def change_sample_width(filename, dst_width=2,out_format = 'wav'):
  sound = AudioSegment.from_file(filename, format = out_format)
  sound = sound.set_sample_width(dst_width)
  sound.export(filename, format=out_format)   

# stretch an wav file randomly
# read all the wav file in "base_dir" , stretch them randomly
# sr  = sample rate  default = 16000
# dst_filename 
# lower_bound =default 0.7
# upper_bound = default = 1.3
# audio that stretched will be saved as the original filename plus "0" , for example, original filename  = asd.wav  dst_filename will be asd0.wav

def random_stretch(base_dir, lower_bound=0.7, upper_bound= 1.3, sr=16000, sample_width = 2):
  random = np.random.RandomState(0)
  for path, pathname, filenames in os.walk(base_dir):
    for filename in filenames:
      if filename.endswith('wav'):
        speed = round(random.uniform(lower_bound,upper_bound),3) 
        y, sr = librosa.load(os.path.join(base_dir,filename),sr = sr)
        y_stretch = librosa.effects.time_stretch(y, speed)
        temp_filename  = filename.split('.wav')[0] + '0' + '.wav'
        dst_name = os.path.join(path,temp_filename)
        librosa.output.write_wav(dst_name, y_stretch, sr=sr)
        change_sample_width(dst_name)


  
if __name__ == "__main__":
  random_stretch('./test/')

      


       
