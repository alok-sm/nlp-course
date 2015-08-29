from preprocess import *
from process import *

if __name__ == "__main__":
	docList = []
	query = raw_input("Enter query string: ")
	with open("../cricket-dataset/50-overs/Linear/Linear-all.txt") as data_file:
		comments = json.load(data_file)
		docs = corpus_preprocess(comments)
	query = document_preprocess(query)
	for d in docs:
		docList.append(tf(d))
	A =  tfidf_and(query,docList)
	B = tfidf_or(query,docList)
	print A
	print B
	#print tf_and(query,docList)
	#print tf_or(query,docList)
	print "\nRanking with AND contraint\n"
	j = 0
	for i in A:
		j += 1
		print str(j)+": "+str(comments[i])
	print "\n-----------------------------------------------------------------------------------------------"
	print "\nRanking with OR contraint\n"
	j = 0
	for i in B:
		j += 1
		print str(j)+": "+str(comments[i])
