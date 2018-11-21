#!/usr/bin/python
# 02/14/2015 typed in from listing

import os, sys, os.path, hashlib, datetime


# function printDirectory:
# prints out a report of checksums for the fiels in each subdirectory
def printDirectory(subdir, path):

	# print only folders

	
	outfile = open(path + os.path.sep + "chksumReports" + os.path.sep + str(datetime.date.today()) + "_" + subdir + "_checksumList.txt", "a+")

	fullAddress = path + os.path.sep + subdir
	print fullAddress
	dirs = os.listdir( fullAddress )


	# This would print all the files and directories
	# I haven't checked for subdirectories because there aren't any in the case of the ssda data directories
	for file in dirs:
		   #print "\n" + file
		   checksumValue = hashlib.sha1(file).hexdigest()
		   #print checksumValue
   
		   outfile.write(file + ": " + checksumValue + "\n")

	outfile.close()

	return (x);



path = os.getcwd()
print "path: " + path

pathString = path.split(os.path.sep)

directory = pathString[len(pathString)-1]



# print only folders
for x in os.listdir(path):
	if os.path.isdir(x):
		printDirectory(x, path)
		


