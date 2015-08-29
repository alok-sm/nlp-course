import json
from nltk.tokenize import RegexpTokenizer
from nltk.stem import *
import itertools

def document_preprocess(doc):
	# print doc
	tokenizer = RegexpTokenizer(r"[a-zA-Z0-9']+")
	stemmer = SnowballStemmer('english')
	doc = remove_aliases(doc.lower())
	# print doc
	doc = tokenizer.tokenize(doc)
	stopword_list=[
		"a",
		"the",
		"and",
		"an",
		"it",
		"has",
		"this",
		"that",
		"that's",
		"i",
		"is",
		"me",
		"myself",
		"you",
		"your",
		"yours",
		"yourself",
		"yourselves",
		"he",
		"him",
		"his",
		"himself",
		"she",
		"her",
		"hers",
		"herself",
		"it",
		"it's"
	]
	doc = [stemmer.stem(word) for word in doc]
	doc = [word for word in doc if word not in stopword_list]

	document = []
	for word in doc:
		document.append(word)
		if(word == "four" or word == "six"):
			document.append("boundary")
	doc = [word[:-2] if word.endswith("'s") else word for word in document]
	return doc

def remove_aliases(comment):
	aliases = {
		"dot ball" : "0 run",
		"no run" : "0 run",
		"single" : "1",
		"double" : "2",
		"4" : "four",
		"6" : "six"
	}
	for alias in aliases.keys():
		if(alias in comment):
			comment.replace(alias, aliases[alias])
	return comment

def corpus_preprocess(comments):
	comments = [
		document_preprocess(comment) for comment in comments
	]
	return comments