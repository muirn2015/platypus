import numpy as np

pnt=np.array([1,2])
org_pnt=np.array([0,0])
end_pnt=np.array([4,0])
vecu=np.subtract(pnt,org_pnt)
vecv=np.subtract(end_pnt, org_pnt)

magu = np.sqrt(np.sum(np.square(vecu)))
magv = np.sqrt(np.sum(np.square(vecv)))

cos0=np.sum(np.multiply(vecu,vecv))/(magv*magu)
if (cos0<=0):
	print magu
else:
	coslen=cos0*magu
	dist=np.sqrt(np.sum(np.square(magu)-np.square(coslen)))
	print dist
