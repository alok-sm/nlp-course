import gensim
def create(sentences):
	trigrams = {}
	sentences = [["token_start"] + sentence for sentence in sentences]

	for sentence in sentences:
		for i, j, k in zip(sentence[:-2], sentence[1:-1], sentence[2:]):
			key = (i, j, k)
			if key in trigrams.keys():
				trigrams[key] += 1
			else:
				trigrams[key] = 1

	pair = []
	return trigrams

temp = 0
D = 0
Z=0
vec = []
vec2 = []
model = gensim.models.Word2Vec(words, size=8)
Data = []
for wi,wj in pair:
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
		vec.append(1-D/Z)
	vec2.append((model.similarity(wi,wj)+1)/2)
	print wi+" "+wj+" "+vec2[-1])
	Data.append([wi,wj,vec2[-1]])
f1 = open("results.csv", "w")
for k, v in trigram.items():
	f1.write( ",".join(list(k)) + "," + v + "\n")
f1.close()
f1 = open("results2.csv", "w")
for it in range(len(pair)):
	f1.write(pair[i1[0]]+","+ pair[it[1]]+","+ vec[it]+"," vec2[it]+ "\n")
f1.close()

	
	
	 
