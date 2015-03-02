from abc import ABCMeta, abstractmethod
from random import shuffle

import math

class Grid:
	__metaclass__ = ABCMeta
	def __init__(self):
		self.sensors = {}
		self.sensorList = []

	def iterate(self):
		for sensor in self.sensorList:
			sensor.iterate(self)
		return self.updateLocations()

	def updateLocations(self):
		newPositions = {}
		changed = False
		for sensor in self.sensorList:
			if sensor.update():
				changed = True
			cell = newPositions.get((sensor.x, sensor.y), [])
			cell.append(sensor)
			newPositions[(sensor.x, sensor.y)] = cell
		self.sensors = newPositions
		return changed

	def add(self, sensor):
		x, y = math.floor(sensor.x), math.floor(sensor.y)
		key = (x, y)
		value = self.get(key)
		value.append(sensor)
		self.sensors[key] = value
		self.sensorList.append(sensor)
		return True
	
	def get(self, location):
		return self.sensors.get(location, [])

	def remove(self, sensor):
		key = (sensor.x, sensor.y)
		value = self.sensors[key]
		value.remove(sensor)
		self.sensors[key] = value
		self.sensorList.remove(sensor)

	def toString(self):
		orderedList = sorted(self.sensorList, key = lambda x: x.x)
		orderedList = sorted(orderedList, key = lambda x: x.y)
		printStuff = []
		for sensor in orderedList:
			printStuff.append(str(sensor.x) + ", " + str(sensor.y))
		return "\n".join(printStuff)