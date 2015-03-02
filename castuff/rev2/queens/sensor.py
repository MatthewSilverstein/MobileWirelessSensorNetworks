from random import randint
import numpy as np
class Sensor:

	def __init__(self, rc, rs, moveMax, x, y, weights=[8, 4, 2, 1], M=2):
		self.rc = rc					# communication radius
		self.rs = rs					# sensing radius
		self.weights = weights
		self.moveCount = 0
		self.moveMax = moveMax
		self.x, self.y = x, y
		self.xlast, self.ylast = 0, 0
		self.M = M
		self.xmoves, self.ymoves = 0, 0
		self.neighbours = None
		self.moveLocation = None

	def iterate(self, grid):
		self.moveBack(grid)
		self.setDesiredMoveLocation(grid)
		self.checkBlock(grid)
		if self.xmoveback:
			self.xmoves = -self.xlast
		if self.ymoveback:
			self.ymoves = -self.ylast

	def setDesiredMoveLocation(self, grid):
		xn, xp, yn, yp = 0, 0, 0, 0
		rs, rc = self.rs, self.rc
		for i in range(-rc, rc + 1):
			for j in range(-rc, rc + 1):
				distance = max(abs(i), abs(j))
				weight = self.weights[distance - 1]
				sensors = grid.get((self.x + i, self.y + j))
				numSensors = len(sensors)
				totalWeight = weight * numSensors
				if i < 0:
					xn += totalWeight
				elif i > 0:
					xp += totalWeight
				if j < 0:
					yn += totalWeight
				elif j > 0:
					yp += totalWeight
		if self.xlast == 0:
			xmoves = xp - xn
		elif self.xlast == -1:
			xmoves = xp * self.M - xn
		elif self.xlast == 1:
			xmoves = xp - xn * self.M
		if xmoves > 0:
			xmoves = -1
		elif xmoves < 0:
			xmoves = 1

		if self.ylast == 0:
			ymoves = yp - yn
		elif self.ylast == -1:
			ymoves = yp * self.M - yn
		elif self.ylast == 1:
			ymoves = yp - yn * self.M
		if ymoves > 0:
			ymoves = -1
		elif ymoves < 0:
			ymoves = 1
		self.xmoves, self.ymoves = xmoves, ymoves

	def checkBlock(self, grid):
		if self.xmoves != 0:
			if self.isEmptyX(grid, self.rc - 1, self.xmoves):
				self.xmoves = 0
		if self.ymoves != 0:
			if self.isEmptyY(grid, self.rc - 1, self.ymoves):
				self.ymoves = 0

	def countSensors(self, grid, x1, y1, rx, ry):
		count = 0
		for i in range(rx + 1):
			for j in range(ry + 1):
				count += len(grid.get((x1 + i, y1 + j)))
		return count


	def isEmptyX(self, grid, r, direction):
		ox, oy = min(0, -r * direction), -self.rc
		return 1 == self.countSensors(grid, self.x + ox, self.y + oy, r, 2 * self.rc) 
		i = 0
		empty = True
		rc = self.rc
		count = 0
		while(i <= r):
			j = 0
			while(-rc <= j <= rc ):
				count += len(grid.get((self.x + i * direction, self.y + j)))
				if count > 1:
					return False
				j+=1
			i+=1
		return True

	def isEmptyY(self, grid, r, direction):
		ox, oy = -self.rc, min(0, -r * direction)
		return 1 == self.countSensors(grid, self.x + ox, self.y + oy, 2 * self.rc, r) 
		j = 0
		empty = True
		rc = self.rc
		count = 0
		while(j <= r):
			i = 0
			while(-rc <= i <= rc ):
				count += len(grid.get((self.x + i, self.y + j * direction)))
				if count > 1:
					return False
				i+=1
			j+=1
		return True

	def moveBack(self, grid):
		self.xmoveback = False
		self.ymoveback = False
		if self.xlast != 0:
			if self.isEmptyX(grid, self.rc, self.xlast):
				self.xmoveback = True
		if self.ylast != 0:
			if self.isEmptyY(grid, self.rc, self.ylast):
				self.ymoveback = True

	def update(self):
		move = self.xmoves != 0 or self.ymoves != 0
		if move:
			if self.moveCount >= self.moveMax:
				self.xmoves = 0
				self.ymoves = 0
				move = False
			else:
				self.moveCount+=1
		self.x = self.x + self.xmoves
		self.y = self.y + self.ymoves
		self.xlast = self.xmoves
		self.ylast = self.ymoves
		self.xmoveback = False
		self.ymoveback = False
		return move