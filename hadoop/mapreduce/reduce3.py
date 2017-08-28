#!/usr/bin/python3
import sys
import os
import math

documents = {}
word_count = {}
idfs = {}

for line in sys.stdin:
    line = line.rstrip('\n')
    line = line.rstrip()
    word = line.split("\t")[0]

    line2 = line.split("\t")[1]
    line2arr = line2.split(" ")

    # print(line2arr)

    idf = line2arr[0]

    idfs[word] = idf

    freq = int(line2arr[2])

    if word in word_count.keys():
        word_count[word] += freq
    else:
        word_count[word] = freq

    doc_info_string = ''
    doc_info_string += (str(line2arr[1]) + ' ')
    doc_info_string += (str(line2arr[2]) + ' ')
    doc_info_string += (str(line2arr[3]) + ' ')

    if word in documents.keys():
        documents[word] += doc_info_string
    else:
        documents[word] = doc_info_string

# print("IDFS BITCH\n")
# print(idfs)
# print("DOCUMENTS WHORE\n")
# print(documents)

for word in documents:
    print (word, '\t', idfs[word], word_count[word], documents[word].rstrip())
