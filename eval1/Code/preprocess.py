import json
from nltk.tokenize import RegexpTokenizer
from nltk.stem import *
import enchant

def document_preprocess(doc):
	stemmer = SnowballStemmer('english')
	boundry_list = ["four", "six", "boundari", "boundary", "6", "4"]
	stopword_list = ["a","the","and","for", "an","it", "has", "i","is","for","me","myself","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","it's","its"]
	# stopword_list = []
	dictionary = enchant.Dict("en_US")
	doc = [stemmer.stem(word) if dictionary.check(word) else word for word in doc]
	doc = [word for word in doc if word not in stopword_list]
	doc = [word if word not in boundry_list else "boundary" for word in doc]
	return doc

def corpus_preprocess(comments):
	tokenizer = RegexpTokenizer(r"[a-zA-Z0-9']+")
	comments = [
		document_preprocess(
			tokenizer.tokenize(
				comment.lower()
			)
		)
		for comment in comments
	]
	return comments

with open("../cricket-dataset/50-overs/Linear/Linear-all.txt") as data_file:
	comments = json.load(data_file)
	print(corpus_preprocess(comments)[0])
	

