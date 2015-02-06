from random import randint
import numpy as np
class Sensor:

	def __init__(self, rc, rs, moveMax, dampening, x, y):
		self.rc = rc		# communication radius
		self.rs = rs		# sensing radius
		self.currentLocation = (x, y)	
		self.moveCount = 0
		self.moveMax = moveMax
		self.desiredMoveLocation = None
		self.neighbours = None
		self.oldV = np.zeros(2)
		self.dampening = dampening
		# other variables for setting desiredMoveLocation

		self.moveLocation = None
		self.conflictResolved = False
		self.conflict = 0	