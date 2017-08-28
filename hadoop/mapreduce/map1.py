#!/usr/bin/python3
import re
import sys

stopdict = [] #List of Stopwords
stop = open('stopwords.txt', "r") #open stopwords file as read-only
for word in stop:
	word = re.sub(r'[^a-zA-Z0-9]+', '', word)
	stopdict.append(word) #add each stopword in the .txt to the list
for line in sys.stdin:
	first_line = line #get doc_id
	first_line = first_line.strip('\n')
	second_line = sys.stdin.readline() #get the doc title
	third_line = sys.stdin.readline()
	combined = second_line +" "+ third_line
	words = combined.split()
	#print ("doc_id" + "\t" + first_line, sep = '')
    #print the doc id in key \t value form
	for word in words:
		word = word.lower() #make the word case insensitive
		word = re.sub(r'[^a-zA-Z0-9]+', '', word)
        #Remove any non-alphanumerics
		if word not in stopdict and word != ' ' and word:
        #only print word if not in the stopwords and not empty string
			print(word, "\t", first_line, sep='')
#print the word followed by the doc_ID
