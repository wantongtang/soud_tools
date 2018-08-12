
import os
import librosa 
import sys

base_dir = sys.argv[1] #'../data7/chxb'
max_duration = 0
max_duration_filename = ''
min_duration = 1000
min_duration_filename =''

k = 0
g = 0
h = 0

  


all_duration = 0
for fpath,pathname,filenames in os.walk(base_dir):
  for filename in filenames:
    k+=1
    if filename.endswith('wav') and (  "_background_noise_" not in fpath):
      y, sr = librosa.load(os.path.join(fpath,filename),sr=16000)    
      temp_duration = librosa.get_duration(y,sr=sr)
      all_duration += temp_duration
      if temp_duration > max_duration:
        max_duration  =  temp_duration
        max_duration_filename = os.path.join(fpath,filename)
      if temp_duration < min_duration:
        min_duration  = temp_duration
        min_duration_filename  =  os.path.join(fpath,filename)

      if temp_duration >1.6:
#        os.system('rm -rf %s '%os.path.join(fpath,filename))
        g+=1
      if temp_duration >4:
        h+=1

      print(temp_duration)
print('max')
print( max_duration)
print('maxfile')
print (max_duration_filename)

print('min')
print(min_duration)
print('min file')
print(min_duration_filename)
print('avarage duration = %s'%(str(all_duration/k)))

print('>1.5: %d'%g)
print('>4: %d'%h)
