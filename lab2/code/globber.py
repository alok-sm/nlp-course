import glob
from nltk.tokenize import sent_tokenize, word_tokenize
import codecs

filenames = glob.glob("../NDTV_mobile_reviews_Classified/*/*.txt") + glob.glob("../NDTV_mobile_reviews_Classified/*.txt")

text = ""

for filename in filenames:
	with codecs.open(filename, "r", "utf-8") as file:
		text += file.read()
text.replace("\n", " ")

sentences = [word_tokenize(sentence) for sentence in sent_tokenize(text)]

