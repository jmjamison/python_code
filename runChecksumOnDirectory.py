#!/usr/bin/python
#
# This creates a file, named: today's date_bkup_directory_checksumList.txt
#       that lists each file in the directory and it's checksum
#     15feb13jmj - runs from the directory to be checked
#
# 20181119jmj fix code for python 3.7x - change print statements and add the uft-8 encoding line 25
#

import os, sys, os.path, hashlib, datetime

path = os.getcwd()
print(path)
pathString = path.split(os.path.sep)

directory = pathString[len(pathString)-1]
print(directory)

dirs = os.listdir( path )

outfile = open(path + str(os.path.sep) + str(datetime.date.today()) + "_" + directory  + "_checksumList.txt", "a+")

# This would print all the files and directories
for file in dirs:
   checksumValue = hashlib.sha1(str(file).encode('utf-8')).hexdigest()   
   outfile.write("\n" + file + ": " + checksumValue)

outfile.close()
