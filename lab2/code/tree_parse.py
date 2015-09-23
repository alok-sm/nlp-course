import nltk 
with open('../NDTV_mobile_reviews_Classified/karbonn-kt-21/karbonn-kt-21-review.txt', 'r') as f:
    sample = f.read()

def nltk_tree_to_list(node):
	if(type(node) is nltk.tree.Tree):
		if(len(node.leaves()) == 1):
			res = [(node.leaves()[0][0], node.label())]
		else:
			res = []
			for child in node:
				res += nltk_tree_to_list(child)
		return res
	else:
		return [node]

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)
chunked_sentences = list(chunked_sentences)
chunked_sentences = reduce(lambda x, y : x + y, [nltk_tree_to_list(child) for child in chunked_sentences])

print chunked_sentences