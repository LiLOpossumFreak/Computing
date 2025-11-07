#File Handling (Mr Simpson's example program)

#-------------Main Program-----------------
#open file
import time
with open("higher/SDD/File_Handling/SampleFile.txt") as readfile:
    #filecontents = readfile.read()
    nextLine = readfile.readline()
    while nextLine != "":
        print(nextLine.strip())
        time.sleep(2)
        nextLine = readfile.readline()