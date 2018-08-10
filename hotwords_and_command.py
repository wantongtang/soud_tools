import os
import sys

from xatx_data_preprocess import get_name



def rename_hotword(src_dir, dst_dir):
  for path, pathname, filenames in os.walk(src_dir):
    person_name = get_name()
    k = 0
    for filename in filenames:
      print(filename)
      if "a" in filename.split("wav")[0]:
        print("chxb")
        dir1 = "chxb"
      elif "b" in filename.split('wav')[0]:
        print("other")
        dir1 = "other"
      src_file = os.path.join(path,filename)  
      dst_dir_tmp = os.path.join(dst_dir,dir1)
      dst_filename = person_name + str(k) + '.wav'
      dst_file = os.path.join(dst_dir_tmp,dst_filename)
      os.system('cp -rf  %s %s'%(src_file,dst_file))
      k+= 1


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("usage: python hotword_and_command.py  src_dir dst_dir \n that will rename all the wav file from src_dir to dst_dir ")
  else:
    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    rename_hotword(src_dir,dst_dir)

