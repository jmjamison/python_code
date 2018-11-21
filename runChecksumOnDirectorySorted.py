#!/usr/bin/python
#
# This creates a file, named: today's date_bkup_directory_checksumList.txt
#       that lists each file in the directory and it's checksum
#     15feb13jmj
#  In order to have the list in alphebetic order, use a list, sortFile, and sort() routines
#

import os, sys, os.path, hashlib, datetime

path = os.getcwd()
print path
pathString = path.split(os.path.sep)

directory = pathString[len(pathString)-1]

dirs = os.listdir( path )

outfile = open(path + os.path.sep + str(datetime.date.today()) + "_" + directory  + "_checksumList.txt", "w+")

sortFile = []

# This would print all the files and directories
for file in dirs:
   checksumValue = hashlib.sha1(file).hexdigest()   
   sortFile.append(file + ": " + checksumValue + "\n")


sortFile.sort()
#print(sortFile)

outfile.writelines(sortFile)

outfile.close
