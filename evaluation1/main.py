import re
from nltk.stem.snowball import SnowballStemmer
import nltk
import random
import sys
from cleanup import cleanup

def main():
	with open(sys.argv[1], 'r') as input_file:
		text = cleanup(input_file.read())

		stemmer = SnowballStemmer("english")

		words = [map(stemmer.stem, nltk.word_tokenize(it)) for it in nltk.sent_tokenize(text)]

		_unigramCounts={}
		for vec in words:
			for it in vec:
				if it not in _unigramCounts.keys():
					_unigramCounts[it]=1
				else:
					_unigramCounts[it]+=1
		threshold=5

		unigramCounts = {}

		unigramCounts[u"_UNKNOWN"] = 0

		for k, v in _unigramCounts.items():
			if v<threshold:
				unigramCounts[u"_UNKNOWN"] += v
			else:
				unigramCounts[k] = v

		vocab = unigramCounts.keys()

		print random.shuffle(vocab)
		
		pairs = list(
			zip(
				sorted(vocab, key=lambda k: random.random())[0:10], 
				sorted(vocab, key=lambda k: random.random())[0:10]
			)
		)

		print pairs


if __name__ == '__main__':
	main()