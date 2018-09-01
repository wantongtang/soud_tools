
import os
import librosa 
import sys



def get_duration(base_dir):

  max_duration = 0
  max_duration_filename = ''
  min_duration = 1000
  min_duration_filename =''

  k = 0
  g = 0
  h = 0
  
  du15 = 0
  

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
  
        if temp_duration >1.504:
#        os.system('rm -rf %s '%os.path.join(fpath,filename))
          g+=1
        if temp_duration <0.4:
          h+=1
        if temp_duration != 1.5:
          du15+=1
#          os.system("cp %s %s"%(os.path.join(fpath,filename),'./xatx_low_vol_data/'))

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
  print('<0.4: %d'%h)
  print("not 1.5 %d"%du15)

if __name__=="__main__":
  if len(sys.argv) != 2:
    print("usage: python get_max_duration src_dir ")
  else:
    base_dir = sys.argv[1]
    get_duration(base_dir)
