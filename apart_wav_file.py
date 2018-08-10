# read a wav and apart them into to part, each part is in the same length

from pydub import AudioSegment
import os
import librosa


def apart_wav_file(filename):
  sound1 = AudioSegment.from_file(filename, format="wav")
  leng = int( len(sound1)/2)
  sound2 = sound1[:leng]
  sound3 = sound1[-leng:]
  os.system('rm -rf %s'%filename)
  filename1 = filename.split('.wav')[0]+'1'+'.wav'
  filename2 = filename.split('.wav')[0]+'2'+'.wav'
  sound2.export(filename1,format='wav')
  sound3.export(filename2,format='wav')


if __name__ == '__main__':
  # delete all the file that duration more than 5s and apart them into two part
  k = 0  
  base_dir = '../mydata/other/'
  for path,pathname,filenames in os.walk(base_dir):
    for filename in filenames:
      y, sr = librosa.load(os.path.join(base_dir,filename),sr = 16000)
      duration = librosa.get_duration(y,sr=sr)
      if duration >3:
        k+=1      
        print('filename: %s duration : %s'%(filename,duration))
        apart_wav_file(os.path.join(base_dir,filename))

  print(k)
#      apart_wav_file(os.path.join(base_dir,filename))
#  apart_wav_file('./test.wav')
