import sys
import os

arguments = sys.argv
count = len(arguments)

#########################################
# Set of fucntions to check valid input #
#########################################

#only one input allowed, name of file counts as argument
if count != 2:
    print("to many inputs")
    quit()

#checks to see if files exists
try:
    currentFile = open(arguments[1],'rb')
except:
    print "original file does not exist, program requires a file"
    quit()

size = os.stat(currentFile.name).st_size    #size of the file in bytes
os.mkdir("recv")                            #create sub directory
os.chdir("./recv")                          #change to recv directory
dumpFile = open(currentFile.name,'wb+')     #create file in subdirectory

iterations = size/1000                      #used for iterations of for loop

#read and write 1000 bytes at a time
for x in range(0,iterations):
    dumpFile.write(currentFile.read(1000))








