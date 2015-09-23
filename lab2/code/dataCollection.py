import os

data = ""
for x in os.walk('../NDTV_mobile_reviews_Classified'):
	for text in x[2]:
		with open(x[0]+'/'+text, 'r') as f:
			data += f.read()
#data.decode("utf8","ignore")
with open("data.txt",'w') as f:
	f.write(data)		
