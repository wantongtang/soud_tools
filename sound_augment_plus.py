'''
Author: Scott H. Hawley

Based on paper,  
A SOFTWARE FRAMEWORK FOR MUSICAL DATA AUGMENTATION
Brian McFee, Eric J. Humphrey, and Juan P. Bello
https://bmcfee.github.io/papers/ismir2015_augmentation.pdf

This script can either be called as a standalone to operate on sound files (e.g., .wav),
or it can be imported & called from elsewhere, e.g. prep_data.py.  

If you plan on using prep_data.py, then don't call this as a standalong. just let prep_data 
do its thing, unless you really want to hear what the augmented data files sound like.
'''
from __future__ import print_function
import numpy as np
import librosa
from random import getrandbits
import sys, getopt, os
#from scipy.signal import resample     # too slow
import scipy


def random_onoff():                # randomly turns on or off
    return bool(getrandbits(1))


# returns a list of augmented audio data, stereo or mono
def augment_data(y, sr, n_augment = 0, allow_speedandpitch = True, allow_pitch = True,
    allow_speed = True, allow_dyn = True, allow_noise = True, allow_timeshift = True, tab=""):

    mods = [y]                  # always returns the original as element zero
    length = y.shape[0]

    for i in range(n_augment):
#        print(tab+"augment_data: ",i+1,"of",n_augment)
        y_mod = y
        count_changes = 0

        # change speed and pitch together
        if (allow_speedandpitch) and random_onoff():   
            length_change = np.random.uniform(low=0.9,high=1.0)
            speed_fac = 1.0  / length_change
#            print(tab+"    resample length_change = ",length_change)
            tmp = np.interp(np.arange(0,len(y),speed_fac),np.arange(0,len(y)),y)
            #tmp = resample(y,int(length*lengt_fac))    # signal.resample is too slow
            minlen = min( y.shape[0], tmp.shape[0])     # keep same length as original; 
            y_mod *= 0                                    # pad with zeros 
            y_mod[0:minlen] = tmp[0:minlen]
            count_changes += 1

        # change pitch (w/o speed)
        if (allow_pitch) and random_onoff():   
            bins_per_octave = 24        # pitch increments are quarter-steps
            pitch_pm = 4                                # +/- this many quarter steps
            pitch_change =  pitch_pm * 2*(np.random.uniform()-0.5)   
#            print(tab+"    pitch_change = ",pitch_change)
            y_mod = librosa.effects.pitch_shift(y, sr, n_steps=pitch_change, bins_per_octave=bins_per_octave)
            count_changes += 1

        # change speed (w/o pitch), 
        if (allow_speed) and random_onoff():   
            speed_change = np.random.uniform(low=1.0,high=1.2)
#            print(tab+"    speed_change = ",speed_change)
            tmp = librosa.effects.time_stretch(y_mod, speed_change)
            minlen = min( y.shape[0], tmp.shape[0])        # keep same length as original; 
            y_mod *= 0                                    # pad with zeros 
            y_mod[0:minlen] = tmp[0:minlen]
            count_changes += 1

        # change dynamic range
        if (allow_dyn) and random_onoff():  
            dyn_change = np.random.uniform(low=0.5,high=1.1)  # change amplitude
#            print(tab+"    dyn_change = ",dyn_change)
            y_mod = y_mod * dyn_change
            count_changes += 1

        # add noise
        if (allow_noise) and random_onoff():  
            noise_amp = 0.005*np.random.uniform()*np.amax(y)  
            if random_onoff():
#                print(tab+"    gaussian noise_amp = ",noise_amp)
                y_mod +=  noise_amp * np.random.normal(size=length)  
            else:
#                print(tab+"    uniform noise_amp = ",noise_amp)
                y_mod +=  noise_amp * np.random.normal(size=length)  
            count_changes += 1

        # shift in time forwards or backwards
        if (allow_timeshift) and random_onoff():
            timeshift_fac = 0.01 *2*(np.random.uniform()-0.5)  # up to 20% of length
#            print(tab+"    timeshift_fac = ",timeshift_fac)
            start = int(length * timeshift_fac)
            if (start > 0):
                y_mod = np.pad(y_mod,(start,0),mode='constant')[0:y_mod.shape[0]]
            else:
                y_mod = np.pad(y_mod,(0,-start),mode='constant')[0:y_mod.shape[0]]
            count_changes += 1

        # last-ditch effort to make sure we made a change (recursive/sloppy, but...works)
        if (0 == count_changes):
            print("No changes made to signal, trying again")
            mods.append(  augment_data(y, sr, n_augment = 1, tab="      ")[1] )
        else:
            mods.append(y_mod)

    return mods



def auto_aug(in_dir,dst_dir, n_augment):
    np.random.seed(1)
    for path, pathname, filenames in os.walk(in_dir):
        for filename in filenames:
            if filename.endswith('wav'):
                print(filename)
                y, sr = librosa.load(os.path.join(path,filename), sr=None)
                mods = augment_data(y, sr, n_augment=n_augment, allow_timeshift=False )
                for i in range(len(mods)-1):
                    filename_no_ext = os.path.splitext(os.path.join(dst_dir,filename))[0]
                    ext = os.path.splitext(os.path.join(path,filename))[1]
                    outfile = filename_no_ext+str(i+1)+ext
                    #librosa.output.write_wav(outfile, mods[i+1],sr)
                    scipy.io.wavfile.write(outfile,sr,np.int16(mods[i+1]*32768))



if __name__ == "__main__":
    if len(sys.argv) !=4:
        print("usage python sound_augment_plus.py base_dir  n_augment  \n it will augment all the file in the basedir")
        sys.exit()
    else:
        base_dir = sys.argv[1]
        dst_dir = sys.argv[2]
        n_augment = int(sys.argv[3])
        auto_aug(base_dir,dst_dir,n_augment)

'''
    import argparse
    parser = argparse.ArgumentParser(description='Perform data augmentation')
    parser.add_argument("-t", "--test", help="test on sample data (takes precedence over other args)", action="store_true")
    parser.add_argument("N", help="number of augmentations to generate",type=int)
    parser.add_argument('file', help="sound files to augment", nargs='*')   
    args = parser.parse_args()
    main(args)

'''



