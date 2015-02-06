import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def iterate(Z):
	#Count neighbours
	N= (Z[:-2, :-2] + Z[:-2, 1:-1] + Z[:-2,2:] + 
						Z[1:-1, :-2] + Z[1:-1, 2:] +
						Z[2: , :-2] + Z[2: ,1:-1] + Z[2: ,2:])

	#Apply rules
	birth = (N==3) & (Z[1:-1,1:-1] == 0)
	survive = ((N==2) | (N==3)) & (Z[1:-1,1:-1]==1)
	Z[...] = 0
	Z[1:-1,1:-1][birth | survive] = 1
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
		iterate(Z)
	plt.show()

def initZ(size):
	Z = np.random.randint(0,2, size)
	return Z

def main(*args):
	Z = initZ((20,20))
	gameOfLife(Z,steps = 100)
	#basics2()

if __name__ == "__main__":
	main()