#  /tmp/extract_loudest_section/gen/bin/extract_loudest_section 

import os

base_dir = '../mydata/chxb/'
dst_dir = './chxv_extracted/'
for filepaths ,pathname,filenames in os.walk(base_dir):
  for filename in filenames:
    print(filename)
    os.system(' /tmp/extract_loudest_section/gen/bin/extract_loudest_section %s %s'%(os.path.join(base_dir,filename),dst_dir))
