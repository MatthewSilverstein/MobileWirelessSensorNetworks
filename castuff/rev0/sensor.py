from random import randint
class Sensor:

	def __init__(self, rc, rs, maxMoves, lowerK, upperK, x, y):
		self.rc = rc
		self.rs = rs
		self.lowerK = lowerK
		self.upperK = upperK
		self.x = x
		self.y = y
		self.maxMoves = maxMoves
		self.moves = 0
		self.Q1 = [0, 1]
		self.Q2 = [0, 2]
		self.Q3 = [0, 3]
		self.Q4 = [0, 4]

	def iterate(self, grid, step):
		if step % 2 == 0:
			self.calculateQuadrants(grid)
			self.calculateMinMax()
			self.calculateDirection()

	def calculateQuadrants(self, grid):
		if not self.canMove():
			self.setQuadrants(0, 0, 0, 0)
			return
		rc = self.rc
		sumQ1 = sumQ2 = sumQ3 = sumQ4 = 0
		q1oy = -rc + self.y
		q1ox = 1 + self.x
		q2oy = -rc + self.y
		q2ox = -rc + self.x
		q3oy = 0 + self.y
		q3ox = -rc + self.x
		q4oy = 1 + self.y
		q4ox = 0 + self.x
		for y in range(0, rc + 1):
			for x in range(0, rc):
				distance = max(rc - y, x + 1)
				weight = rc + 1 - distance
				sumQ1 += weight * len( grid.get((q1ox + x, q1oy + y)))

		for y in range(0, rc):
			for x in range(0, rc + 1):
				distance = max(rc - y, rc - x)
				weight = rc + 1 - distance
				sumQ2 += weight * len( grid.get((q2ox + x, q2oy + y)))

		for y in range(0, rc + 1):
			for x in range(0, rc):
				distance = max(y, rc - x)
				weight = rc + 1 - distance
				sumQ3 += weight * len( grid.get((q3ox + x, q3oy + y)))

		for y in range(0, rc):
			for x in range(0, rc + 1):
				distance = max(y + 1, x)
				weight = rc + 1 - distance
				sumQ4 += weight * len( grid.get((q4ox + x, q4oy + y)))
		self.setQuadrants(sumQ1, sumQ2, sumQ3, sumQ4)

	def setQuadrants(self, Q1, Q2, Q3, Q4):
		self.Q1[0] = Q1
		self.Q2[0] = Q2
		self.Q3[0] = Q3
		self.Q4[0] = Q4

	def calculateMinMax(self):
		minQ = [self.Q1]
		if minQ[0][0] > self.Q2[0]:
			minQ = [self.Q2]
		elif minQ[0][0] == self.Q2[0]:
			minQ.append(self.Q2)
		if minQ[0][0] > self.Q3[0]:
			minQ = [self.Q3]
		elif minQ[0][0] == self.Q3[0]:
			minQ.append(self.Q3)
		if minQ[0][0] > self.Q4[0]:
			minQ = [self.Q4]
		elif minQ[0][0] == self.Q4[0]:
			minQ.append(self.Q4)

		maxQ = [self.Q1]
		if maxQ[0][0] < self.Q2[0]:
			maxQ = [self.Q2]
		elif maxQ[0][0] == self.Q2[0]:
			maxQ.append(self.Q2)
		if maxQ[0][0] < self.Q3[0]:
			maxQ = [self.Q3]
		elif maxQ[0][0] == self.Q3[0]:
			maxQ.append(self.Q3)
		if maxQ[0][0] < self.Q4[0]:
			maxQ = [self.Q4]
		elif maxQ[0][0] == self.Q4[0]:
			maxQ.append(self.Q4)
		self.minQ = minQ[randint(0, len(minQ) - 1)]
		self.maxQ = maxQ[randint(0, len(maxQ) - 1)]

	def calculateDirection(self):
		# check if direction is in threshhold
		if self.lowerK >= self.minQ[0] and self.upperK <= self.maxQ[0]:
			# choose which of two locations to choose
			if self.minQ[1] == 1:
				self.moveLocation = (self.x + 1 , self.y - randint(0, 1))
			elif self.minQ[1] == 2:
				self.moveLocation = (self.x - randint(0, 1), self.y - 1)
			elif self.minQ[1] == 3:
				self.moveLocation = (self.x - 1, self.y + randint(0, 1))
			else:
				self.moveLocation = (self.x + randint(0, 1), self.y + 1)
		else:
			self.moveLocation = (self.x, self.y)

	def canMove(self):
		if self.maxMoves == 0:
			return True
		return self.moves < self.maxMoves

class StationarySensor(Sensor):

	def __init__(self, rc, lowerK, upperK, x, y):
		Sensor.__init__(self, rc, lowerK, upperK, x, y)

	def iterate(self, grid, step):
		self.moveLocation = (self.x, self.y)
		pass