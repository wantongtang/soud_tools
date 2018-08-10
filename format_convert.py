##########################
#dr.mark.schultz@gmail.com#
#20160626####################
###########################
import os
import glob
from pydub import AudioSegment
import argparse
import audioread
import time


# from predict import  *



"""
Dependencies:
1. gcc
2. pydub (sudo pip install pydub), see https://github.com/jiaaro/pydub
3. ffmpeg (brew install libav --with-libvorbis --with-sdl --with-theora)
4. audioread (sudo pip install audioread)
Default will spit out wav file slices of 2 second duration, in 16bit/mono/44.1kHz sample rate (Useful for the
Analog Elektron Rytm drum machine).
Will chop up the input file and spit out slices along its length until it reaches the end of the file.
Can input/output in any format that ffmpeg supports.
example usage:
python SliceAudio.py -i xyz.m4a -f m4a -b 2 -s 11025 -l 10000
python SliceAudio.py -h

To do:
    add support to set output destination folder
    add support to only output glued reversed chunks (i.e., turn off full output)
    allow naming of glued reverse-granule file

"""

#parse command line input
PARSER = argparse.ArgumentParser(description=
								"""
								Generates one-shot samples from long audio files in batch.\n
								Also reverses each slice and saves them to file.
								Glues the reversed slices together in input order and saves them to file.
								e.g., song sequence 'ABC'becomes 'A-reversedB-revCrev' (not 'CBA').
								Interesting granulation effects can be had if you slice up the file into 
								tiny segments and slide the window along a full slice length
								Email: dr.mark.schultz@gmail.com for questions/feedback.
								""")
PARSER.add_argument('-i', '--infiles', help=
					"""
					Name of input files. Can use e.g., '*.mp3' to bring up all mp3 files in a path.
					"""
					, default="", required=False)
#					, nargs='+', required=False)
PARSER.add_argument('-c', '--channels', help=
					"""
					Number of output channels per file. '1', mono (default); '2', stereo.
					""", default = 1, required=False)
PARSER.add_argument('-o', '--out_format', help=
					"""
					Output format of files. 'wav' .wav (default); 'mp3', .mp3 etc.
					""", default = 'wav', required=False)
PARSER.add_argument('-b', '--sample_width', help=
					"""
					Number of bytes in each sample. Options are: '1'=8-bit; '2'=16-bit (default); '4'=32-bit.  Note program will exit with a 'key error' if an option other than 1, 2 or 4 is selected.
					""", default = 2, required=False)
PARSER.add_argument('-s', '--sample_rate', help=
					"""
					Sample rate of slices. '44100' (44.1kHz, CD quality); '48000' (default, DVD quality). Other common rates are '22050', '24000', '12000' and '11025'.
					""", default = 16000, required=False)
PARSER.add_argument('-l', '--sample_slice_length_ms', help=
					"""
					Length of sample slices in milliseconds. '2000' (default, 2 seconds).
					""", default = 60000, required=False)
PARSER.add_argument('-w', '--window_slide_ms', help=
					"""
					Move the slice window along this many milliseconds to start the next slice (a 'sliding window'). '2000' (default, 2 seconds).
					""", default = 1000, required=False)

PARSER.add_argument('-O',
					'--output_dir',
					type = str,
					default = "./",
					help = """
					Out put dir
					""")
PARSER.add_argument('-I',
					"--input_dir",
					default = "",
					help = "input dir for multi files")
ARGS = PARSER.parse_args()


def format_convert(in_file,out_format,out_rate,out_channels,out_bits):
	
	fileName, fileExtension = os.path.splitext(in_file)
	print(in_file)
	with audioread.audio_open(in_file) as f:
		sound = AudioSegment.from_file(in_file, fileExtension.replace('.','').lower())
		sound = sound.set_frame_rate(int(out_rate))
		sound = sound.set_sample_width(int(out_bits))
		sound = sound.set_channels(int(out_channels))
		sound.export(ARGS.output_dir+fileName.split('/')[-1]+'.'+ out_format, format=out_format)



if __name__ == '__main__':
	

	if ARGS.input_dir:
		for in_file in os.listdir(ARGS.input_dir):
			format_convert(ARGS.input_dir+in_file,ARGS.out_format,ARGS.sample_rate,ARGS.channels,ARGS.sample_width)	

	else:
		
		format_convert(ARGS.infiles,ARGS.out_format,ARGS.sample_rate,ARGS.channels,ARGS.sample_width)	
