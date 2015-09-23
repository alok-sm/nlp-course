import math
import numpy as np
from scipy.optimize import minimize as myMin
class MyMaxEnt():
	def __init__(self,histLst,funcs):	# Init With Both List Of Hist,Tag Pairs, And Functions (Callbacks).
		self.model=np.array([0.0]*len(funcs))
		self.histLst=histLst
		self.funcs=funcs
		self.Y=[]	# IMPORTANT Fill This Up With All Possible Tags. IMPORTANT
		self.trainEx=[]
		self.testEx=[]
		# Above Line To Be Used If Both Train And Test Are In The Same File.
		self.total=0.0
		self.currentHist={}
	def create_dataset(self):	# Dataset In The Form Of List Of Individual Examples, Each Of Which Is A Dict, With Keys Being The Possible Tags, And Values The f-vectors Of That Example. One Special Key Is "_exOP", Whose Value Is The Actual Tag Of The Example.
		self.testList=self.histLst[int(0.8*len(histLst)):]
		self.histLst=self.histLst[:int(0.8*len(histLst))]
		# Above 2 Lines To Be Used If Both Train And Test Are In The Same File.
		for it in self.histLst:
			hst=list(it)
			self.trainEx.append({})
			for jt in self.Y:
				self.trainEx[-1][jt]=[]
				for kt in self.funcs:
					self.trainEx[-1][jt].append(kt(hst[:4],jt))
			self.trainEx[-1]["_exOP"]=hst[4]
	def cost(self,model):
		self.model=model
		totalCost=0.0
		for i in range(len(self.trainEx)):
			totalCost+=dotP(self.trainEx[i][self.trainEx["_exOP"]])
			nF=0.0
			for k, v in self.trainEx[i].items():
				if k!="_exOP":
					nF+= math.exp(self.dotP(v))
			totalCost-=math.log(nF)
		return totalCost
	def classify(self,h):	# Call On History Tuples To Test For, Returns Tag.
		allTags=[]
		self.histConvert(list(h))
		self.setTot()
		for it in self.Y:
			allTags.append(self.p_y_given_x(h,it))
		manC=0
		maxV=0
		for it in range(len(allTags)):
			if maxV<allTags[it]:
				maxV=allTags[it]
				maxC=it
		return self.Y[it]
	def dotP(self,h):
		cumul=0.0
		for ln in range(len(self.model)):
			self.cumul+=self.model[ln]*h[ln]
		return cumul
	def setTot(self):
		self.total=0.0
		for v in self.currentHist.values:
			self.total+=math.exp(dotP(v))
	def p_y_given_x(self,h,tag):
		return math.exp(self.dotP(self.currentHist[tag]))/self.total
	def train(self):	# Call To Train Machine
		self.create_dataset()
		params=myMin(self.cost,self.model,method="L-BFGS-B", jac=gradient)	# Add	jac=gradient	As A Parameter For The Optional Part.
		self.model=params.x
		fp=open("maxEntModel.csv","w")
		fp.write(",".join(list(self.model)))
		fp.close()
	def gradient(self,model):
		self.model=model
		totalCost=0.0
		for i in range(len(self.trainEx)):
			totalCost+=self.trainEx[i][self.trainEx["_exOP"]]
			nF=0.0
			tmpTot=0.0
			for k, v in self.trainEx[i].items():
				if k!="_exOP":
					tmp=math.exp(dotP(v))
					tmpTot+=tmp
					nF+=v*tmp
			totalCost-=(float(nF)/tmpTot)
		return totalCost
	def histConvert(self,h):
		for it in self.Y:
			self.currentHist[it]=[]
			for jt in self.funcs:
				self.currentHist[it].append(jt(h,it))
	def setModel(self,model):
		self.model=np.array(model)