import re
from nltk.stem.snowball import SnowballStemmer
import nltk
import random
import sys
from cleanup import cleanup
from tweet import create
import gensim
def stem(word):
	stemmer = SnowballStemmer("english")
	stemmer.stem(word)

	if(re.match(r'[\.\?\!\-\_]+', word)):
		return None
	else:
		return word

def main():
	with open(sys.argv[1], 'r') as input_file:
		text = cleanup(input_file.read())

		words = [map(stem, nltk.word_tokenize(it)) for it in nltk.sent_tokenize(text)]

		words = [[x for x in sentence if x is not None] for sentence in words]

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

		while True:
			l1 = sorted(vocab, key=lambda k: random.random())[0:10]
			l2 = sorted(vocab, key=lambda k: random.random())[0:10]
			if(u"_UNKNOWN" not in l1 and u"_UNKNOWN" not in l2):
				break
		
		pairs = list(
			zip(l1, l2)
		)

	temp = 0
	
	vec = []
	vec2 = []
	print words
	model = gensim.models.Word2Vec(words, size=8)
	trigrams=create(words)
	for wi,wj in pairs:
		D = 0
		Z=0
		for k in trigrams.keys():
			temp=0
			if k[1]==wi:
				temp=trigrams[k]
				Z+=trigrams[k]
			if k[1]==wj:
				temp-=trigrams[k]
				Z+=trigrams[k]
			if temp<0:
				temp=-temp
				D+=temp

		vec.append(1-float(D)/Z)
		vec2.append((model.similarity(wi,wj)+1)/2)
	f1 = open("results.csv", "w")
	for k, v in trigrams.items():
		f1.write( ",".join(list(k)) + "," + str(v) + "\n")
	f1.close()
	f1 = open("results2.csv", "w")
	for it in range(len(pairs)):
		f1.write(str(pairs[it][0])+","+ str(pairs[it][1])+","+ str(vec[it])+","+ str(vec2[it])+ "\n")
	f1.close()


if __name__ == '__main__':
	main()