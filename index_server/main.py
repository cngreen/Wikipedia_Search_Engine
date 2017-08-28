from flask import *
from extensions import db
import re
import math

def import_shit():
#imports the data into the server
	#import the page rank file into page_rank, key is docID, value is page_rank
	f = open('./pagerank.out')
	page_rank = {}
	for line in f:
		input_list = line.split(",")
		page_rank[int(input_list[0])] = float(input_list[1])

	#import the stop words file into stop_words list
	f2 = open('stopwords.txt')
	stop_words = []
	for line in f2:
		line = line.rstrip('\n')
		line = re.sub(r'[^a-zA-Z0-9]+', '', line)
		stop_words.append(line)

	#import the inverted index file into inverted_index. key is word, value is a list.
	#first value in the list is the idf eg. inverted_index[word][0] = idf
	#second value in the list is the total number of occurrences eg. inverted_index['word'][1] = numOccurrences
	#third value in the list is the documents associated with the word eg. inverted_index['word'][2] = docs
	#the docs object key is the docID, containing a list with the docOccurrences[0] and the docNormFactor[1]

	## HELPFUL NOTES:
	#	- to access the documents inverted_index['word'][2][docID]
	#	- for key in inverted_index['word'][2] will return all docs that contain the word

	###--- TO-DO: CHANGE THE INPUT FILE TO WHATEVER THE OUTPUT FROM PART 1 is ---###
	f3 = open('outfile.txt')
	inverted_index = {}
	for line in f3:
		docs = {}
		line = line.rstrip('\n')
		line = line.rstrip()
		input_list2 = line.split("\t")[1].split(" ")

		word = line.split("\t")[0].rstrip()
		idf = float(input_list2[1])
		occurrences = int(input_list2[2])
		i = 3
		size = len(input_list2)
		while (i < size):
			docID = int(input_list2[i])
			i += 1
			docOccurrences = int(input_list2[i])
			i += 1
			docNormFactor = float(input_list2[i])
			i += 1
			docs[docID] = [docOccurrences, docNormFactor]
		inverted_index[word] = [idf, occurrences, docs]

	return page_rank, stop_words, inverted_index

page_rank, stop_words, inverted_index = import_shit()

print("WARNING SHIT WAS LOADED")

def parse_query(query):
#parse the query into a list of words
	query.rstrip('\n')
	query.rstrip()
	query_input = query.split(' ')
	query_words = []

	for w in query_input:
		if w not in stop_words and w != ' ':
			w = re.sub(r'[^a-zA-Z0-9]+', '', w)
			if w != '':
				w = w.lower()
				query_words.append(w)

	return query_words

def get_all_docs_list(word, inverted_index):
#returns a list of all docs that contains the given word
	docs = []
	if word not in inverted_index.keys():
		return docs
	for key in inverted_index[word][2]:
		docs.append(key)
	print docs
	return docs

def inter(l1, l2):
#theoretically will find the intersection of the list of docs
	return list(set(l1) & set(l2))


def find_documents(query_words, inverted_index):
#theoretically returns the docs that contain all of the query words
	all_docs = []
	i = 0
	for word in query_words:
		if(i == 0):
			all_docs = get_all_docs_list(word, inverted_index)
		else:
			all_docs = inter(get_all_docs_list(word, inverted_index), all_docs)
		i = i + 1

	return all_docs

def cosine_similarity(inverted_index, query_words, docID):
#See Piazza post: https://piazza.com/class/iroxiazhljc4n0?cid=1890
	total_doc_norm_factor = 0
	total_query_norm_factor = 0
	doc_dot_query = 0

	for word in set(query_words):
		 term_occurrences = query_words.count(word)
		 term_idf = inverted_index[word][0]
		 doc_occurrences = inverted_index[word][2][docID][0]
		 doc_norm_factor = inverted_index[word][2][docID][1]

		 total_doc_norm_factor = doc_norm_factor
		 total_query_norm_factor += (pow(term_occurrences, 2) * pow(term_idf, 2))
		 doc_dot_query += (term_occurrences * pow(term_idf, 2) * doc_occurrences)

	total_doc_norm_factor = math.sqrt(total_doc_norm_factor)
	total_query_norm_factor = math.sqrt(total_query_norm_factor)

	similarity = 0

	if (total_doc_norm_factor != 0 and total_query_norm_factor != 0):
		similarity = (doc_dot_query / (total_query_norm_factor * total_doc_norm_factor))

	return similarity

def calculate_score(weight, query_words, docID, inverted_index, page_rank):
	if docID not in page_rank.keys():
		doc_page_rank = 0
	else:
		doc_page_rank = page_rank[docID]
	tfIdf = cosine_similarity(inverted_index, query_words, docID)
	score = (weight * doc_page_rank) + ((1 - weight) * tfIdf)

	return score

def cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1

##--------------------------------------------------------------------------------------------------------------------------
##--------------------------------------------------------------------------------------------------------------------------
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
	tojson = []
	weight = float(request.args.get('w'))
	query = request.args.get('q')

	query_words = parse_query(query)
	print("\nquery_words:")
	print(query_words)

	documents = find_documents(query_words, inverted_index)
	print("\ndocuments:")
	print(documents)

	results = []
	# a list of the documents and the score in a list
	# results[i][0] = docID
	# results[i][1] = score

	for doc in documents:
		score = calculate_score(weight, query_words, doc, inverted_index, page_rank)
		results.append([doc, score])

	results.sort(cmp)
	print("\nresults:")
	print(results)

	for r in results:
		tojson.append({'docid': int(r[0]), 'score': float(r[1])})

	return(jsonify(hits=tojson))
