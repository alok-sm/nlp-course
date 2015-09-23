''' Put Functions Here As A List '''
''' Read File And Form HistList '''
maxEnt=MyMaxEnt(histList,funcs)
maxEnt.train()	# To Train
# fp=open("maxEntModel.csv","r")	# To Use Pickled Model
# model=[float(it) for it in fp.read().split(",")]
# maxEnt.setModel(model)
# fp.close()
aCount=0.0
tCount=0.0
for it in maxEnt.testList:
	tCount+=1
	if maxEnt.classify(it[:4])==it[4]:
		aCount+=1
print "Accuracy Is:",aCount/tCount