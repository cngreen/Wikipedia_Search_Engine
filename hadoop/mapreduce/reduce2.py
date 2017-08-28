#!/usr/bin/python3
import sys
import os
import math

documents = {}
normalization_factors = {}

for line in sys.stdin:
    line = line.rstrip('\n')
    line = line.rstrip()
    docID = line.split("\t")[0]
    docID = docID.strip('\n')
    line2 = line.split("\t")[1]
    line2 = line2.strip('\n')

    doc_info_array = line2.split(" ")
    norm_factor = 0
    freq = float(doc_info_array[0])
    idf = float(doc_info_array[1])

    norm_factor = (pow(freq, 2) * pow(idf, 2))

    if docID in normalization_factors.keys():
        normalization_factors[docID] += norm_factor
    else:
        normalization_factors[docID] = norm_factor

    if docID in documents.keys():
        documents[docID] += (" " + line2)
    else:
        documents[docID] = line2

for doc in documents:
    print (doc, '\t', end="")
    print (str(normalization_factors[doc]), end=' ')
    print (documents[doc])