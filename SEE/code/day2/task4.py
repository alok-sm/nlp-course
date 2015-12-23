import numpy as np
from math import *
import json
import neurolab as nl
inputLst = json.load(open("vectors.txt", "r"))
numerator = 0.0
denominator = 0.0
eq_vectors = 0.0
targets = json.load(open("fv.txt", "r"))
testX = inputLst[int(0.75*len(inputLst)):]
inputLst = inputLst[:int(0.75*len(inputLst))]
testY = targets[int(0.75*len(targets)):]
targets = targets[:int(0.75*len(targets))]
results = []
net = nl.net.newff([[0.0, 1.0] for _ in xrange(26)], [20, 22])
net.train(inputLst, targets, show = 1, epochs = 300)
ret = net.sim(testX)
for it in range(len(ret)):
	temp = [int(jt > 0.6) for jt in ret[it]]
	results.append(temp)
	eq_vectors += int(temp == testY[it])
	numerator += sum([x[0] == x[1] == 1 for x in zip(temp, testY[it])])
	denominator += sum([x == 1 for x in testY[it]])

print "number of matching 1's:    ", numerator/denominator
print "number of matching vectors:", eq_vectors/len(ret)
