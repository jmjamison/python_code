#!/usr/bin/python
#
# This creates a file, named: today's date_bkup_directory_checksumList.txt
#       that lists each file in the directory and it's checksum
#     15feb13jmj - runs from the directory to be checked
#
# 20181119jmj fix code for python 3.7x - change print statements and add the uft-8 encoding line 25
# this version, python 3.7 reads external dir
#
# add later choice of checksup method

import os, sys, os.path, hashlib, datetime

directoryToCheck = os.path.normpath(input("Directory to checksum: "))

if os.path.isdir(directoryToCheck): 
    print("Yes, it's a directory: " + directoryToCheck + "\n Checksup with MD5")

else:
    print(directoryToCheck + " is not a directory, try again")

pathString = directoryToCheck.split(os.path.sep)

# os.path.normpath mornalize path name, clean up trailing / if there is on
#fileDirectory = os.path.normpath(directoryToCheck)
fileDirectory = os.path.normpath(pathString[len(pathString)-1])
print(" Directory: " + fileDirectory)


dirs = os.listdir( directoryToCheck )


outfile = open(fileDirectory + "_" + str(datetime.date.today()) + "_" + "_MD5_checksumList.txt", "a+")
print(outfile)

# was first using sha1 but changed to md5 since that is what Dataverse uses
for file in dirs:
   checksumValue = hashlib.md5(str(file).encode('utf-8')).hexdigest()   
   outfile.write("\n" + file + ": " + checksumValue)
   #print("\n" + file)

outfile.close()
