import nltk 
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import MyMaxEnt
import os


#test_sen = raw_input("Enter a sentence : ")
#with open('../NDTV_mobile_reviews_Classified/karbonn-kt-21/karbonn-kt-21-review.txt', 'a') as f:
#    f.write("\n"+test_sen)


with open('data.txt', 'r') as f:
    sample = f.read()



def get_functions():

	def is_first_word(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(index == 0)

	def is_last_word(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(index + 1 == len(sentence))

	def capital_first_letter(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(sentence[index][0].isupper())

	def follows_noun(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(tag_minus_1[0] == 'N')

	def is_stopword(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(sentence[index][0] in stopwords.words('english'))

	def is_stemmed(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		stemmer = SnowballStemmer("english")
		return int(stemmer.stem(sentence[index][0]) == sentence[index][0] )

	def is_number(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(sentence[index][0].replace(".", "").replace(",", "").isdigit())

	def is_abbrevation(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		return int(sentence[index][0].replace(".", "").isupper())

	def is_country(history, tag):
		tag_minus_2, tag_minus_1, sentence, index = history
		countries = ["Afghanistan","Aland Islands","Albania","Algeria","American Samoa","AndorrA","Angola","Anguilla","Antarctica","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Bouvet Island","Brazil","British Indian Ocean Territory","Brunei Darussalam","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Canada","Cape Verde","Cayman Islands","Central African Republic","Chad","Chile","China","Christmas Island","Cocos (Keeling) Islands","Colombia","Comoros","Congo","Congo, The Democratic Republic of the","Cook Islands","Costa Rica","Cote D'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Falkland Islands (Malvinas)","Faroe Islands","Fiji","Finland","France","French Guiana","French Polynesia","French Southern Territories","Gabon","Gambia","Georgia","Germany","Ghana","Gibraltar","Greece","Greenland","Grenada","Guadeloupe","Guam","Guatemala","Guernsey","Guinea","Guinea-Bissau","Guyana","Haiti","Heard Island and Mcdonald Islands","Holy See (Vatican City State)","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran, Islamic Republic Of","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jersey","Jordan","Kazakhstan","Kenya","Kiribati","Korea, Democratic People'S Republic of","Korea, Republic of","Kuwait","Kyrgyzstan","Lao People'S Democratic Republic","Latvia","Lebanon","Lesotho","Liberia","Libyan Arab Jamahiriya","Liechtenstein","Lithuania","Luxembourg","Macao","Macedonia, The Former Yugoslav Republic of","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Martinique","Mauritania","Mauritius","Mayotte","Mexico","Micronesia, Federated States of","Moldova, Republic of","Monaco","Mongolia","Montserrat","Morocco","Mozambique","Myanmar","Namibia","Nauru","Nepal","Netherlands","Netherlands Antilles","New Caledonia","New Zealand","Nicaragua","Niger","Nigeria","Niue","Norfolk Island","Northern Mariana Islands","Norway","Oman","Pakistan","Palau","Palestinian Territory, Occupied","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Pitcairn","Poland","Portugal","Puerto Rico","Qatar","Reunion","Romania","Russian Federation","RWANDA","Saint Helena","Saint Kitts and Nevis","Saint Lucia","Saint Pierre and Miquelon","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia and Montenegro","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Georgia and the South Sandwich Islands","Spain","Sri Lanka","Sudan","Suriname","Svalbard and Jan Mayen","Swaziland","Sweden","Switzerland","Syrian Arab Republic","Taiwan, Province of China","Tajikistan","Tanzania, United Republic of","Thailand","Timor-Leste","Togo","Tokelau","Tonga","Trinidad and Tobago","Tunisia","Turkey","Turkmenistan","Turks and Caicos Islands","Tuvalu","Uganda","Ukraine","United Arab Emirates","United Kingdom","United States","United States Minor Outlying Islands","Uruguay","Uzbekistan","Vanuatu","Venezuela","Viet Nam","Virgin Islands, British","Virgin Islands, U.S.","Wallis and Futuna","Western Sahara","Yemen","Zambia","Zimbabwe"]
		return int(sentence[index][0].lower() in [country.lower() for country in countries])



	return [
		is_first_word,
		is_last_word,
		capital_first_letter,
		follows_noun,
		is_stopword,
		is_stemmed,
		is_number,
		is_abbrevation,
		is_country
	]

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
		return [(node[0], 'OTHER')]

def create_history(sentence):
	history = [
		('*', '*', sentence, 0),
		('*', sentence[0][1], sentence, 1)
	]

	for i in range(2, len(sentence)):
		history += [(sentence[i-2][1], sentence[i-1][1], sentence, i)]

	# history = [
	# 	('*', '*', 0),
	# 	('*', sentence[0][1], 1)
	# ]

	# for i in range(2, len(sentence)):
	# 	history += [(sentence[i-2][1], sentence[i-1][1], i)]


	return history[:len(sentence)]

sentences = nltk.sent_tokenize(sample)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)
chunked_sentences = list(chunked_sentences)
chunked_sentences = [nltk_tree_to_list(child) for child in chunked_sentences]

words = reduce(lambda x, y : x + y, chunked_sentences)

tags = [word[1] for word in words]

tagset = set(tags)
# print tags
history = reduce(lambda x, y : x + y, [create_history(sentence) for sentence in chunked_sentences])


args = list(zip(history, tags))
#print args

maxEnt=MyMaxEnt.MyMaxEnt(args, get_functions())
maxEnt.train()	# To Train
# fp=open("maxEntModel.csv","r")	# To Use Pickled Model
# model=[float(it) for it in fp.read().split(",")]
# maxEnt.setModel(model)
# fp.close()
aCount=0.0
tCount=0.0
for it in maxEnt.testList:
	tCount+=1
	if maxEnt.classify(it[0])==it[1]:
		aCount+=1
print "Accuracy with 20% dataset :",aCount/tCount
