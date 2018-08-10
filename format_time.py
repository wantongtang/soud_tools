# fill the sound to the aimed duration


from pydub import AudioSegment



def  time_regular(wav_filename,time_duration):
  sound = AudioSegment.from_wav(wav_filename)
  if len(sound) < time_duration:
    silent_duration = AudioSegment.silent(duration= (time_duration - len(sound)+1))
    sound = sound + silent_duration 
    sound.export(wav_filename,format = 'wav')



  




if __name__ == "__main__":
  time_duration = 1000 #ms
  wav_filename  = './test.wav'
  time_regular(wav_filename,time_duration) 

  
