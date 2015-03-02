import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
""" This will calculate quadrants with no weighted values""" 
""" Need to pad matrix with rows and columns of zeros at the start and end to account for incomplete quadrants. And then set them back to 0. """


def iterate(Z, rc):
	Q1, Q2, Q3, Q4 = countQuadrantsWeights(Z, rc)
	minQ = findMinQuadrants(Q1, Q2, Q3, Q4)
	maxQ = findMaxQuadrants(Q1, Q2, Q3, Q4)


def countQuadrantsWeights(Z, rc):
	""" Counts quadrants using weights based on distance """
	R,C = Z.shape

	endR = R - 2 * rc
	endC = C - 2 * rc

	#Offsets
	q1or = 0
	q1oc = rc + 1
	q2or = 0
	q2oc = 0
	q3or = rc
	q3oc = 0
	q4or = rc + 1
	q4oc = rc
	Q1 = np.zeros((endR, endC), dtype=int)
	for r in range(0, rc + 1):
		for c in range(0, rc):
			distance = max(rc -r, c + 1)
			weight = rc + 1 - distance
			Q1 += weight * (Z[q1or + r : q1or + endR + r, q1oc + c : q1oc + endC + c])

	Q2 = np.zeros((endR, endC), dtype=int)
	for r in range(0, rc):
		for c in range(0, rc + 1):
			distance = max(rc - r, rc - c)
			weight = rc + 1 - distance
			Q2 += weight * (Z[q2or + r : q2or + endR + r, q2oc + c : q2oc + endC + c ])

	Q3 = np.zeros((endR, endC), dtype=int)
	for r in range(0, rc + 1):
		for c in range(0, rc):
			distance = max(r, rc - c)
			weight = rc + 1 - distance
			print 'w = ', weight, ', r = ', r, ',c = ',c
			Q3 += weight * (Z[q3or + r : q3or + endR + r,q3oc + c : q3oc + endC + c])	

	Q4 = np.zeros((endR, endC), dtype=int)
	for r in range(0, rc):
		for c in range(0, rc + 1):
			distance = max(r + 1, c)
			weight = rc + 1 - distance
			Q4 += weight * (Z[q4or + r : q4or + endR + r, q4oc + c : q4oc + endC + c ])

	return Q1, Q2, Q3, Q4

def findMinQuadrants( Q1, Q2, Q3, Q4):
	endR, endC = Q1.shape
	MinQ = [[0 for i in range(endC)] for j in range(endR)]
	for r in range(endR):
		for c in range(endC):
			list1 = [(Q1[r,c], 1), (Q2[r,c], 2), (Q3[r,c], 3), (Q4[r,c], 4)]
			random.shuffle(list1)
			minV = list1[0]
			for i in range(1, 4):
				if minV[0]> list1[i][0]:
					minV = list1[i]
			MinQ[r][c] = minV
	return MinQ


def findMaxQuadrants( Q1, Q2, Q3, Q4):
	endR, endC = Q1.shape
	MaxQ = [[0 for i in range(endC)] for j in range(endR)]
	for r in range(endR):
		for c in range(endC):
			list1 = [(Q1[r,c], 1), (Q2[r,c], 2), (Q3[r,c], 3), (Q4[r,c], 4)]
			random.shuffle(list1)
			maxV = list1[0]
			for i in range(1, 4):
				if maxV[0]< list1[i][0]:
					maxV = list1[i]
			MaxQ[r][c] = maxV
	return MaxQ

def countQuadrantsNoWeights(Z, rc):
	R,C = Z.shape
	Z1 = np.zeros((R - rc, C - rc + 1), dtype=int)
	for r in range(0, rc + 1):
		for c in range(0, rc):
			Z1 += (Z[ r: R - rc + r, c : C - (rc - 1) + c])

	Z2 = np.zeros((R - rc + 1, C - rc), dtype=int)
	for r in range(0, rc):
		for c in range(0, rc + 1):
			Z2 += (Z[ r : R - (rc - 1) + r, c : C - rc + c ])

	endR = R - 2 * rc
	endC = C - 2 * rc
	#Offsets

	q1or = 0
	q1oc = rc + 1
	q2or = 0
	q2oc = 0
	q3or = rc
	q3oc = 0
	q4or = rc + 1
	q4oc = rc

	Q1 = Z1[q1or : endR + q1or, q1oc : endC + q1oc]
	Q2 = Z2[q2or : endR + q2or, q2oc : endC + q2oc]
	Q3 = Z1[q3or : endR + q3or, q3oc : endC + q3oc]
	Q4 = Z2[q4or : endR + q4or, q4oc : endC + q4oc]
	print "************* Q1 **************"
	print Q1
	print "************* Q2 **************"
	print Q2
	print "************* Q3 **************"
	print Q3
	print "************* Q4 **************"
	print Q4
	return Z

def gameOfLife(Z, steps = 0):
	size = Z.shape
	dpi = 72.0
	figsize = size[1]/float(dpi),size[0]/float(dpi)
	frames = steps + 1
	interval=300
	mode = 'loop'
	fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
	fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
	im=plt.imshow(Z,interpolation='nearest', cmap=plt.cm.gray_r)
	plt.xticks([]), plt.yticks([])
	for i in range(steps):
		iterate(Z, 4)
	#plt.show()

def initZ(size):
	Z = np.random.randint(0,2, size)
	return Z


def pad(Z, rc):
	R,C = Z.shape
	for i in range(rc):
		Z = np.insert(Z, C, values=0, axis = 1)
	for i in range(rc):
		Z = np.insert(Z, 0, values=0, axis = 1)
	for i in range(rc):
		Z = np.insert(Z, R, values=0, axis = 0)
	for i in range(rc):
		Z = np.insert(Z, 0, values=0, axis = 0)
	return Z

def initTest1():
	Z = np.zeros((20,20), dtype=int)
	Z[0] = 1
	Z[19] = 1
	Z[10] = 1
	Z[:,10] = 1
	Z[:,0] = 1
	Z[:,19] = 1
	#Z[0,0] = 0
	#Z[1,0] = 0
	#Z[2,0] = 0
	#Z[3,0] = 0
	#Z[4,0] = 0
	return Z

def main():
	rc = 4
	Z = initZ((20,20))
	Z = initTest1()
	print Z
	Z = pad(Z, rc)
	print Z.shape
	#countQuadrantsNoWeights(Z, rc)
	iterate(Z, rc)
	countQuadrantsWeights(Z, rc)
	#gameOfLife(Z,steps = 1)
	#basics2()

if __name__ == "__main__":
	main()