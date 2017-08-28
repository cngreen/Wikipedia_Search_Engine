#!/usr/bin/python3
import sys
import os
import math

wordDict = {}
output = {}

out_file = open('total_document_count.txt', "r")
total_num_docs = int(out_file.readline())


for line in sys.stdin:
    line = line.rstrip('\n')
    line = line.rstrip()
    word = line.split("\t")[0]
    line2 = line.split("\t")[1]

    if word in wordDict.keys():
        wordDict[word] += (" " + line2)
    else:
        wordDict[word] = line2

#print(wordDict)
#print(wordDict['airplanes'])

for word in wordDict:
    text = wordDict[word]
    docsArray = text.split(" ")
    size = len(docsArray)
    #print(size)
    num_docs_with_term = size / 2
    idf = math.log10(total_num_docs/num_docs_with_term)

    output[word] = [idf, text]

#print(output)

stringList = []

for word in output:
    myString = ''
    myString += str(word)
    myString += '\t'
    myString += str(output[word][0])
    myString += ' '
    myString += str(output[word][1])
    stringList.append(myString)

#print(stringList)

for word in stringList:
    newWord = word.split('\t')[0] #Get the word by splitting by tab
    line2 = word.split('\t')[1] #Line 2 = norm_factor, doc_id, freq in doc_id, (repeated)
    outlist = line2.split(' ') #split via spaces
    num_docs = int(len(outlist)) #Get the number of documents given
    i = 1
    #print ("NUM DOCS: ", num_docs)
    while i < num_docs:
        print(outlist[i], sep='', end='\t'), #print doc_id followed by tab
        i += 1
        print(outlist[i], outlist[0], newWord, sep=' ') #print frequency, norm_factor, word
        i +=1
