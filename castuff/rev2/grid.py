from abc import ABCMeta, abstractmethod
from random import shuffle
class Grid:
	__metaclass__ = ABCMeta
	def __init__(self, width = 0, height = 0, capacity = 0):
		self.sensors = {}
		self.sensorList = []
		self.width = width
		self.height = height
		self.capacity = capacity

	def iterate(self, step):
		for sensor in self.sensorList:
			sensor.iterate(self, step)
		if step % 2 == 1:
			return self.updateLocations()
		return True

	def updateLocations(self):
		def add(self, newPositions, maxCapacities, sensor):
			newPosition = sensor.moveLocation
			if newPosition != (sensor.x, sensor.y) and self.inBoundaries(newPosition):
				newStuffInCell = newPositions.get(newPosition, [])
				if (self.capacity == 0) or maxCapacities.get(newPosition, 0) < self.capacity:
					newStuffInCell.append(sensor)
					sensor.x, sensor.y = newPosition
					newPositions[newPosition] = newStuffInCell
					maxCapacities[newPosition] = maxCapacities.get(newPosition, 0) + 1
					sensor.moves += 1
					return True
			value = newPositions.get((sensor.x, sensor.y), [])
			value.append(sensor)
			newPositions[sensor.x, sensor.y] = value
			return False

		shuffle(self.sensorList)
		newPositions = {}
		maxCapacities = {}
		for location in self.sensors:
			maxCapacities[location] = len(self.sensors[location])
		changed = False
		for sensor in self.sensorList:
			changed2 = add(self, newPositions, maxCapacities, sensor)
			if changed2:
				changed = True
		self.sensors = newPositions
		return changed

	def add(self, sensor):
			key = (sensor.x, sensor.y)
			if self.inBoundaries(key):
				value = self.get(key)
				if self.cellHasRoom(value):
					value.append(sensor)
					self.sensors[key] = value
					self.sensorList.append(sensor)
					return True
			return False
	
	def get(self, location):
		return self.sensors.get(location, [])

	def remove(self, sensor):
		key = (sensor.x, sensor.y)
		value = self.sensors[key]
		value.remove(sensor)
		self.sensors[key] = value
		self.sensorList.remove(sensor)

	def inBoundaries(self, location):
		if self.width == 0 and self.height == 0:
			return True
		return 0 <= location[0] < self.width and 0<= location[1] < self.height

	def cellHasRoom(self, cell):
		if self.capacity == 0:
			return True
		return len(cell) < self.capacity

	def toString(self):
		orderedList = sorted(self.sensorList, key = lambda x: x.x)
		orderedList = sorted(orderedList, key = lambda x: x.y)
		printStuff = []
		for sensor in orderedList:
			printStuff.append(str(sensor.x) + ", " + str(sensor.y))
		return "\n".join(printStuff)
