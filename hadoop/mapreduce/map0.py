#!/usr/bin/python3

import sys

num_lines = 0
for line in sys.stdin: #Parse lines
	num_lines += 1 #Each line Add 1
num_docs = int((num_lines) / 3) #3 Lines to Each File
print ("num_docs\t", num_docs) #Print in Key <tab> Value form