import matplotlib.pyplot as plt
import numpy as np
def basics1():
	Z = np.array([  [0,0,0,0,0,0],
					[0,0,0,1,0,0],
					[0,1,0,1,0,0],
					[0,0,1,1,0,0],
					[0,0,0,0,0,0],
					[0,0,00,0,0,0]])

	print Z.dtype #type
	print Z.shape #dimensions

	print Z[0,5] # specific index

	print Z[1:5,1:5] #splice thingy

	A = Z[1:5,1:5]
	print A
	print Z

	print Z.base is None
	print A.base is Z

	N = np.zeros(Z.shape, dtype=int)
	N[1:-1, 1:-1] += (Z[:-2, :-2] + Z[:-2, 1:-1] + Z[:-2,2:] + 
						Z[1:-1, :-2] + Z[1:-1, 2:] +
						Z[2: , :-2] + Z[2: ,1:-1] + Z[2: ,2:])
	print Z
	iterate(Z)
	print Z
	iterate(Z)
	print Z

def iterate(Z):
	N = np.zeros(Z.shape,int)
	N[1:-1, 1:-1] += (Z[:-2, :-2] + Z[:-2, 1:-1] + Z[:-2,2:] + 
						Z[1:-1, :-2] + Z[1:-1, 2:] +
						Z[2: , :-2] + Z[2: ,1:-1] + Z[2: ,2:])
	N_ = N.ravel()
	Z_ = Z.ravel()

	#Apply rules
	R1 = np.argwhere( (Z_==1) & (N_ < 2) )
	R2 = np.argwhere( (Z_==1) & (N_ > 3) )
	R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)))
	R4 = np.argwhere( (Z_==0) & (N_==3) )

	#Set new rules
	Z_[R1] = 0
	Z_[R2] = 0
	Z_[R3] = Z_[R3]
	Z_[R4] = 1

	#Make sure borders stay null
	Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0


def iterate_2(Z):
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


def basics2():
	Z = np.random.randint(0,2, (1024,1024))
	for i in range(100):
		iterate_2(Z)
	size = np.array(Z.shape)
	dpi = 72.0
	figsize = size[1]/float(dpi),size[0]/float(dpi)
	fig = plt.figure(figsize=figsize, dpi=dpi, facecolor="white")
	fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False)
	plt.imshow(Z,interpolation='nearest', cmap=plt.cm.gray_r)
	plt.xticks([]), plt.yticks([])
	plt.show()



basics2()
