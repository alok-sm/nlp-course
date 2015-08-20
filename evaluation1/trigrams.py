def create(sentences):
	trigrams = {}
	sentences = [["token_start", "token_start"] + sentence for sentence in sentences]

	for sentence in sentences:
		for i, j, k in zip(sentence[:-2], sentence[1:-1], sentence[2:]):
			key = (i, j, k)
			if key in trigrams.keys():
				trigrams[key] += 1
			else:
				trigrams[key] = 1

	return trigrams
