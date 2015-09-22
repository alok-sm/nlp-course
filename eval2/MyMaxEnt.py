import math
from scipy.optimize import minimize as myMin
class MyMaxEnt():
	def __init__(self,histLst,funcs):
		self.model=[0.0]*10
		self.histLst=histLst
		self.funcs=funcs
		self.Y=[]
		self.trainEx=[]
		self.create_dataset()
		self.total=0.0
	def create_dataset(self):
		for it in self.histLst:
			self.trainEx.append([]])
			for jt in self.funcs:
				self.trainEx[-1].append(jt(list(it)))
	def cost(self,model):
		self.model=model
		totalCost=0.0
		for i in range(len(self.trainEx)):
			totalCost+=dotP(self.trainEx[i])
			nF=0.0
			for y in Y:
				nF+= math.exp(dotP(self.trainEx[i]))
			nF=math.log(nF)
			totalCost-=nF
		return totalCost
	def classify(self,h):
		allTags=[]
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
	def setTot(self,h):
		self.total=0.0
		for it in Y:
			self.total+=math.exp(dotP(h))
	def p_y_given_x(self,h,tag):
		self.setTot(h)
		return math.exp(self.dotP(h))/self.total
	def train(self):
		params=myMin(self.cost,self.theta,method="L-BFGS-B")
		self.theta=params.x
	def gradient(self,model):
		self.model=model
		totalCost=0.0
		for i in range(len(self.trainEx)):
			totalCost+=trainEx[i]
			nF=0.0
			for y in Y:
				nF+= math.exp(dotP(self.trainEx[i]))
			nF=math.log(nF)
			totalCost-=nF
		return totalCost