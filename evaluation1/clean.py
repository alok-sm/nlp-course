import re
from nltk.stem.snowball import SnowballStemmer
import nltk
import random
def cleanup(text):

	text = text.lower()

	text = re.sub(r"#[^ \n\t]*", "token_hash", text)
	text = re.sub(r"@[^ \n\t]*", "token_handle", text)
	text = re.sub(r"(mailto\:|(news|(ht|f)tp(s?))\://)[^ \n\t]*" , "token_url", text)
	text = re.sub(r"(\:\w+\:|\<[\/\\]?3|[\(\)\\\D|\*\$][\-\^]?[\:\;\=]|[\:\;\=B8][\-\^]?[3DOPp\@\$\*\\\)\(\/\|])(?=\s|[\!\.\?]|$)", "", text)

	emoji_regex = re.compile(u'['
		u'\U0001F300-\U0001F64F'
		u'\U0001F680-\U0001F6FF'
		u'\u2600-\u26FF\u2700-\u27BF]+', 
		re.UNICODE
	)

	text = emoji_regex.sub('', text)

	return text

def main():
	with open("C:\data\\input.txt", 'r') as input_file:
		text = cleanup(input_file.read())
		stemmer = SnowballStemmer("english")
		lst=nltk.sent_tokenize(text)
		words=[]
		for it in lst:
			words.append(stemmer.stem(nltk.word_tokenize(it)))
		vocab=[]
		unigramCounts={}
		for vec in words:
			for it in vec:
				if it not in vocab:
					vocab.append(it)
					unigramCounts[it]=1
				else:
					unigramCounts[it]+=1
		thres=5
		unigramCounts["_UNKNOWN"]=0
		vocab.append("_UNKNOWN")
		for k, v in unigramCounts.items():
			if v<thres:
				unigramCounts["_UNKNOWN"]+=v
				del unigramCounts[k]
				vocab.remove(k)
		pairs=[]
		j=0
		while j<10:
			tmp=[]
			k=len(words)
			l=len(words[random.randint(0,k)])
			tmp.append([k,l])
			while tmp=[k,l]:
				k=len(words)
				l=len(words[random.randint(0,k)])
			tmp.append([k,l])
			pairs.append([words[tmp[0][0]][tmp[0][1]],words[tmp[1][0]][tmp[1][1]]])
			j+=1
		# with open("C:\data\\output.txt", "w") as output_file:
			# output_file.write(text)


if __name__ == '__main__':
	main()