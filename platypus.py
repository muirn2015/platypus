#!/usr/bin/python
import numpy as np

class Entity:
    
    def __init__(self,type = 0):
        print "constructing entity"
        self.type = type

    def setPart(self,partName = 'None'):
        self.partName = partName
    

    def getAttr(self):
        print "entity type = ",Entity.type

class Point(Entity):
    def __init__(self,xyz = [0,0,0]):
        print "constructing point"
        self.xyz = np.array(xyz)
        Entity.__init__(self,type = 1)
        

    def getAttr(self):
        print "point attributes"
        print xyz

class Line(Entity):
    def __init__(self,xyz = [0,0,0],vector = [1,0,0]):
        print "constructing line"
        self.xyz = np.array(xyz)
        self.vector = np.array(vector)
        Entity.__init__(self,type = 2)
        
    def getAttr(self):
        print "line attributes"
        print xyz


def residual(a,b):
	if a.type == 1 and b.type == 1:
		print "point to point"
        	print "residual = ",np.sqrt(np.sum(np.square(a.xyz-b.xyz)))
	elif a.type == 1 and b.type == 2:
        	print "point to line"
        	vecu= np.subtract(a.xyz-b.xyz)
		vecv= np.subtract(b.xyz-b.vector)
		magu = np.sqrt(np.sum(np.square(vecu)))
		magv = np.sqrt(np.sum(np.square(vecv)))
		cos0=np.sum(np.multiply(vecu,vecv))/(magv*magu)
		if (cos0<=0):
			print "residual=", magu
		else:
			coslen=cos0*magu
			dist=np.sqrt(np.sum(np.square(magu)-np.square(coslen)))
			print "residual=", dist
	
	elif a.type == 2 and b.type == 1:
        	print "point to line"
        	vecu= np.subtract(b.xyz-a.xyz)
		vecv= np.subtract(a.xyz-a.vector)
		magu = np.sqrt(np.sum(np.square(vecu)))
		magv = np.sqrt(np.sum(np.square(vecv)))
		cos0=np.sum(np.multiply(vecu,vecv))/(magv*magu)
		if (cos0<=0):
			print "residual=", magu
		else:
			coslen=cos0*magu
			dist=np.sqrt(np.sum(np.square(magu)-np.square(coslen)))
			print "residual=", dist
