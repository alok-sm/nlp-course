def create(sentences):
	trigrams = set()
	for sentence in sentences:
		for i, j, k in zip(sentence[:-2], sentence[1:-1], sentence[2:]):
			trigrams.add((i, j, k))
	return list(trigrams)
