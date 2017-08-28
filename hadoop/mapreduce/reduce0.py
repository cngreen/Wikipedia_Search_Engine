#!/usr/bin/python3

import sys
import collections

count = 0
for line in sys.stdin:
    number = line.split("\t")[1] # split each line and take the key (which is the total number of documents from the mapper)
    count += int(number) #Add mapper's num_docs to running total
directory = 'total_document_count.txt' #Name of File
out_file = open(directory, "w+") #Create file with write privileges
out_file.write(str(count)) #Write Count to File
out_file.close() #Close File