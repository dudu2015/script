# -*- coding: cp936 -*-
import os
import shutil
import re

src = "e:\\SileadVC\\read.h"
dst = "e:\\SileadVC\\readget.h"

dir = "e:\\SileadVC\\"
os.chdir(dir)
print os.curdir

if os.path.exists(src) == True:
 print src,":exists"
 
if os.path.exists(dst) == True:
 print dst,":exists"
 os.remove(dst)

shutil.copy(src, dst)

infile = open(src)
outfile = open("e:\\SileadVC\\readget2.h",'w')
#exp = ".0x98.," for manual mode
#os.system('sed')
pattern = re.compile(r'\{....,0x98\},')
pattern2 = re.compile(r'\{0x..,0xa{8}\},')
line = '{0xf0,0x98},'
#line2 = '{0x00,0x00110075},'
line3 = '{0x00,0xaaaaaaaa},'
flag = 0;
for line in infile.readlines():
    #print line
    match = pattern.match(line)
    if match:
     print line
     flag = 1;   
     print match.group();
     outfile.write(line);
     continue;
    if flag:
     match2 = pattern2.match(line);
     if match2:
        break;
     else:
        outfile.write(line);
#outfile = open("e:\\SileadVC\\readget2.h",'r')
#for line in outfile.readlines():
#    print line
outfile.close()

infile2 = "e:\\SileadVC\\readget2.h"
outfile3 ="e:\\SileadVC\\readget3.h" 
os.system('sed -e /0xf0/d %s > %s' %(infile2,outfile3))
os.system('sed -e $d %s > %s' %(outfile3,infile2))

