from random import randint
import numpy as np

import math

class Sensor:

	#cdistance [0, 1] (how far from rc max distance for critical is)
	def __init__(self, rc, rs, kcover, kdegree, damp, cdistance, moveMax, x, y):
		self.rc = rc					# communication radius
		self.rs = rs					# sensing radius
		self.moveCount = 0
		self.moveMax = moveMax
		self.x, self.y = x, y
		self.xmoves, self.ymoves = 0, 0
		self.kcover = kcover
		self.degree = kdegree
		self.damp, self.cdistance = damp, cdistance
		self.neighbours = [] 
		self.speed = np.asarray((0, 0))
		self.kdegree = (1 - cdistance) ** 2 / (damp ** 2) * kcover
		self.critical = False
		self.fcover, self.fdegree = 0, 0
		self.v = 0
	
	def iterate(self, grid):
		self.findNeighbours(grid)
		if len(self.neighbours) <= self.degree:
			self.critical = True
		self.setDesiredMoveLocation(grid)

	def update(self):
		self.x, self.y = self.x + self.speed[0], self.y + self.speed[1]
		return True

	#this can be made more efficient by doing a left to right sweep in grid instead of individual sensors
	def findNeighbours(self, grid):
		self.neighbours = []
		minX, minY = int(math.floor(self.x - self.rc)), int(math.floor(self.y - self.rc))
		maxX, maxY = int(math.ceil(self.x + self.rc)), int(math.ceil(self.y + self.rc))
		for i in range(minX, maxX):
			for j in range(minY, maxY):
				sensors = grid.get((i, j))
				for sensor in sensors:
					if sensor != self:
						distance = self.distance(sensor)
						if distance <= self.rc:
							self.neighbours.append(sensor)

	def distance(self, other):
		x = self.x - other.x
		y = self.y - other.y
		return ( x**2 + y**2) ** 0.5

	def normalize(self, v):
		norm=np.linalg.norm(v)
		if norm==0: 
			return v
		return v/norm

	def setDesiredMoveLocation(self, grid):
		rc = self.rc
		force = np.asarray((0, 0))
		v1 = np.asarray((self.x, self.y))
		for sensor in self.neighbours:
			distance = self.distance(sensor)
			distance2 = distance ** 2
			v2 = np.asarray((sensor.x, sensor.y))
			v = self.normalize(v1 - v2)
			Fcover = (-self.kcover/distance2) * v
			Fdegree = 0
			fdegree = 0
			if self.critical:
				fdegree = (self.kdegree/distance2)
				Fdegree = (self.kdegree/distance2) * v
			self.fdegree = fdegree
			self.fcover = (-self.kcover/distance2)
			self.v = v
			force += Fcover + Fdegree
		self.speed = force - self.speed * self.damp