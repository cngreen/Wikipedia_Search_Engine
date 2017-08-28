#!/usr/bin/python3
import sys
import os
import math

for line in sys.stdin:
    doc_id, line2 = line.strip('\n').rstrip().split("\t")

    docsArray = line2.split(" ")
    normal    = docsArray[0]

    words = (len(docsArray) - 1) // 3 #integer division
    for i in range(words):
        frequency = docsArray[i*3+1]
        idf       = docsArray[i*3+2]
        word      = docsArray[i*3+3]
        print(word, end='\t')
        print(idf, doc_id.rstrip(), frequency, normal, sep=' ')
