import nltk



def tf(L):
	#L = ast.literal_eval(document.read())
	D = {}
	for i in L:
		for j in i:
			if j not in D:
				D[j] = 0
			D[j] += 1
	return D

def tfidf(query):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		for J in docList:
			idf.append(0)
			if w in J:
				idf[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[w]
		L2.append(tf)
	return topR(L2,10)

def topR(L, n=10):
	return [i for i in (sorted(range(len(L)), key=lambda k: L[k])[:n]) if not L[i] == 0]

def tfidf(query):
	tf = idf = 0
	total = 0
	L2 = []  #List of TFIDF
	idfL = []
	for w in query:
		for J in docList:
			idf.append(0)
			if w in J:
				idf[-1]+= 1

	for J in docList:
		tf=0
		for w in range(len(query)):
			if query[w] in J:
				if not idfL[w] == len(docList):
					tf += J[w]
			else:
				tf=0
				break
		L2.append(tf)
	return topR(L2,10)