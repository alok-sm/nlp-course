import nltk
import math

def tf(L):
	#L = ast.literal_eval(document.read())
	D = {}
	for i in L:
		if i not in D:
			D[i] = 0
		D[i] += 1
	return D

def tf_or(query,docList):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		idfL.append(0)
		for J in docList:
			if w in J:
				idfL[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[query[w]]
		L2.append(tf)
	return topR(L2,10)

def topR(L, n=10):
	return [i for i in (sorted(range(len(L)), key=lambda k: L[k])[::-1][:10]) if not L[i] == 0]

def tf_and(query,docList):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		idfL.append(0)
		for J in docList:
			if w in J:
				idfL[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[query[w]]
			else:
				tf=0
				break
		L2.append(tf)
	return topR(L2,10)

def tfidf_or(query,docList):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		idfL.append(0)
		for J in docList:
			if w in J:
				idfL[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[query[w]] * math.log(len(docList)/idfL[w])
		L2.append(tf)
	return topR(L2,10)

def tfidf_and(query,docList):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		idfL.append(0)
		for J in docList:
			if w in J:
				idfL[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[query[w]] * math.log(len(docList)/idfL[w])
			else:
				tf=0
				break
		L2.append(tf)
	return topR(L2,10)