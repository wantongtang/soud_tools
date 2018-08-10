import wave
import contextlib
import librosa
def get_duration(wav_file):
  y, sr = librosa.load('./test.wav',sr=16000)
  return librosa.get_duration(y,sr=sr)

if __name__ == "__main__":
  y, sr = librosa.load('./test.wav',sr=16000)
  print(librosa.get_duration(y,sr=sr))
  print(  get_duration('./test.wav'))
