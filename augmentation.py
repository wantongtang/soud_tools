import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import librosa
#import matplotlib.pyplot as plt
import os
#import IPython.display as ipd
import scipy

EPS = 1e-8


def get_spectrogram(wav):
    D = librosa.stft(wav, n_fft=480, hop_length=160,
                     win_length=480, window='hamming')
    spect, phase = librosa.magphase(D)
    return spect


def time_shifting(wav, sr):
    start_ = int(np.random.uniform(-4800, 4800))
    print('time shift: ', start_)
    if start_ >= 0:
        wav_time_shift = np.r_[wav[start_:], np.random.uniform(-0.001, 0.001, start_)]
    else:
        wav_time_shift = np.r_[np.random.uniform(-0.001, 0.001, -start_), wav[:start_]]
    #ipd.Audio(wav_time_shift, rate=sr)
    return wav_time_shift




def volume_tuning(wav):
    wav_with_bg = wav * np.random.uniform(0.8, 1.2)
    return wav_with_bg


def main(file_path):
    file_path = file_path
    wav, sr = librosa.load(file_path, sr=None,dtype=np.int16)
    wav = time_shifting(wav, sr)
#    wav = speed_tuning(wav, sr)
    wav = volume_tuning(wav)
    return wav,sr


if __name__ == '__main__':


    wav,sr =  main('./test.wav')
    scipy.io.wavfile.write( './test1.wav',sr,wav)

    
'''     
    
    file_path = r'C:\Users\Administrator\Downloads\chxb\chxb\0lgqh1rv_nohash_0.wav'
    wav,sr = main(file_path)
    scipy.io.wavfile.write('generated_tone.wav', sr, wav)
    data_path = os.listdir(r"C:\Users\Administrator\Downloads\chxb\chxb")
    #print(data_path)
    for i in data_path:
        temp0 = i
        temp = temp0.split(".wav")[0]
        temp = temp.split("_")

        for j in range(1, 10):
            #print("i="+i)
            wav, sr = main(file_path=r"C:\Users\Administrator\Downloads\chxb\chxb"+"\\"+i)
            #scipy.io.wavfile.write(r"C:\Users\Administrator\Downloads\chxb\chxb_augmentation"+"\\"+ temp[0]+"_"+temp[1]+"_"+str(int(temp[2])+9+j)+".wav", sr, wav)
            print(r"C:\Users\Administrator\Downloads\chxb\chxb_augmentation"+"\\"+ temp[0]+"_"+temp[1]+"_"+str(int(temp[2])+9+j)+".wav", sr, wav)

    # print(wav.shape, wav.max(), wav.min())



'''
