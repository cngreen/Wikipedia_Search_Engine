#!/usr/bin/python3
import sys
import collections
import re

wordDict = {}
doc_id = 'this is doc id'
for line in sys.stdin:
	word = line.split("\t")[0] # Get the Word
	word = word.strip('\n')
	word = word.strip(' ')
	doc_id = line.split("\t")[1] # Get the Doc_ID
	doc_id = doc_id.strip('\n')
	doc_id = doc_id.strip(' ')
	if word not in wordDict:
		wordDict[word] = {} # Make a dictionary of dictionaries
		wordDict[word][doc_id] = 1 #Store as #of occurences for Doc, Doc ID
	elif doc_id not in wordDict[word]:
		wordDict[word][doc_id] = 1
	elif word in wordDict: #If the word is in the word dictionary for that Doc
	    wordDict[word][doc_id] += 1

sortedDict = collections.OrderedDict(sorted(wordDict.items()))
for key in sortedDict:
	print (key, end='\t'),
	for value in sortedDict[key]:
		print (value, sortedDict[key][value], end=' '), #print the word, # of occurences in specific doc, then the doc_id
	print ()