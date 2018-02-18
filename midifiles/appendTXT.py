# A python file that appends a text file to
# a master text output file
import sys
import os
import string

inputFile = open(sys.argv[1], 'r')
outputFile = open("masterFile.txt", 'wb')

outputFile.write(inputFile.read())

inputFile.close()
outputFile.close()
