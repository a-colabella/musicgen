# A python file that truncates a CSV file
# to the first track to use for machine learning
import sys
import csv
import string
import os

inputFile = open(sys.argv[1], 'r')
outputFile = open(sys.argv[2], 'r+')

reader = csv.reader(inputFile)

# Note_off_c = 0
# Note_on_c = 1
# Control_c = 2
# Program_c = 3
# Pitch_blend_c = 4

for line in reader:
    line = str(line)

    #new_line = str.replace(line, ', ', '')

    if "Note_off_c" in line:
        new_line = str.replace(line, 'Note_off_c', '0')
        outputFile.write(new_line)
        outputFile.write("\n")
    elif "Note_on_c" in line:
        new_line = str.replace(line, 'Note_on_c', '1')
        outputFile.write(new_line)
        outputFile.write("\n")
    elif "Control_c" in line:
        new_line = str.replace(line, 'Control_c', '2')
        outputFile.write(new_line)
        outputFile.write("\n")
    elif "Program_c" in line:
        new_line = str.replace(line, 'Program_c', '3')
        outputFile.write(new_line)
        outputFile.write("\n")
    elif "Pitch_blend_c" in line:
        new_line = str.replace(line, 'Pitch_blend_c', '4')
        outputFile.write(new_line)
        outputFile.write("\n")


inputFile.close()
outputFile.close()
    
