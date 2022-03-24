# !/usr/bin/python3
import os, sys, os.path, hashlib, datetime, codecs

path = os.getcwd()
print(path)
pathString = path.split(os.path.sep)

directory = pathString[len(pathString)-1]
print(directory)

dirs = os.listdir( path )

outfile = codecs.open(path + str(os.path.sep) + str(datetime.date.today()) + "_" + directory  + "_checksumList.txt", "a+", "utf-8")

#os.chdir("d:\\tmp")
for root, dirs, files in os.walk(".", topdown = True):
    for name in files:
        file = os.path.join(root, name)
        print(file)
        #print(os.path.join(root, name))
        # checksumValue = hashlib.sha1(str(file).encode('utf-8')).hexdigest()   
        checksumValue = hashlib.md5(str(file).encode('utf-8')).hexdigest()   
        print("\n" + file + ": " + checksumValue)
        outfile.write("\n" + file + ": " + checksumValue)
    for name in dirs:
        dir = os.path.join(root, name)
        print(dir)
        #print(os.path.join(root, name))

outfile.close()