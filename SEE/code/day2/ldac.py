import numpy as np
import json
import os
import sys
from sklearn.linear_model import LogisticRegression


f = open(os.devnull, 'w')
sys.stderr = f

def drange(start, stop, step):
	r = start
	while r > stop:
		yield r
		r += step


x = json.load(open("vectors.txt","r"))
y = json.load(open("fv.txt","r"))

x_train = x[:int(len(x)*0.75)]
y_train = y[:int(len(y)*0.75)]

y_train = zip(*y_train)

x_test = x[int(len(x)*0.75):]
y_test = y[int(len(y)*0.75):]


list_lr = [LogisticRegression()]*22

for i in xrange(22):
	list_lr[i].fit(x_train, y_train[i])

max_right = 0
best_threshold = 0.0

for threshold in drange(0.0, -0.0001, -0.00001):
	output = [[int(lr.predict_log_proba(x)[0][0] > threshold) for lr in list_lr] for x in x_test]

	# print output

	temp_right = sum([x[0] == x[1] for x in zip(output, y_test)])
	if(temp_right > max_right):
		max_right = temp_right
		best_threshold = threshold

	# print 
	print temp_right, threshold

# json.dump(output, open('output.txt', 'w'))
# print output
