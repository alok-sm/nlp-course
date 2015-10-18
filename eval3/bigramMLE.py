import nltk
from nltk.corpus import brown
class BigramMLE():
	def __init__(self):
		self.uniDst={}
		self.biDist={}
		self.words=[]
	def train(self,fn=""):
		if fn:
			sents=nltk.sent_tokenize(open(fn,"r").read())
			for st in sents:
				self.words.append(["_start"]+nltk.word_tokenize(st))
		else:
			sents=brown.sents()
			self.words=[]
			for st in sents:
				self.words.append([u"_start"]+st)
		for wl in range(len(self.words)):
			for wt in range(len(self.words[wl])):
				self.words[wl][wt]=self.words[wl][wt].lower()
		for wl in self.words:
			for wt in range(1,len(wl)):
				if self.uniDst.get(wl[wt],"_empty")=="_empty":
					self.uniDst[wl[wt].lower()]=0.0
				self.uniDst[wl[wt]]+=1.0
				if self.biDist.get(wl[wt],"_empty")=="_empty":
					self.biDist[wl[wt]]={}
				if self.biDist[wl[wt]].get(wl[wt-1],"_empty")=="_empty":
					self.biDist[wl[wt]][wl[wt-1]]=0.0
				self.biDist[wl[wt]][wl[wt-1]]+=1.0
	def mle(self, prev ,word):
		word=word.lower()
		prev=prev.lower()
		try:
			return self.biDist[word][prev]/self.uniDst[word]
		except:
			return 10.0**(-5)
	def pSent(self, sent):
		words=["_start"]+nltk.word_tokenize(sent)
		prob=1.0
		for it in range(1,len(words)):
			prob*=self.mle(words[it-1],words[it])
		return prob
