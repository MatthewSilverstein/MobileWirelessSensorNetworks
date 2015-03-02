from sensor import Sensor
import numpy as np
import random
from metrics import totalCoverage
from graphs import graphCoverage
import math

def test1():
	global grid, Kcover
	stepMax = 100
	rc = 3
	rs = 1
	moveMax = 100
	width = 100
	height = 100
	capacity = 1
	Kcover = 4
	dampening = 0.75
	grid = {"width": width, "height": height, "capacity": capacity}
	sensors = initSensors1(rc, rs, moveMax, dampening, width, height)
	for sensor in sensors:
		location = grid.get(sensor.currentLocation, [])
		location.append(sensor)
		grid[sensor.currentLocation] = location
	stepList = []
	totalCoverageList = []
	for step in range(stepMax):
		print "Step:", step
		iterate(sensors)
		totalCoverageList.append(totalCoverage(grid, sensors))
		stepList.append(step)
	graphCoverage(stepList, totalCoverageList)

	print "DONE"

def initSensors1(rc, rs, moveMax, dampening, width = 0, height = 0):
	sensors = []
	offX = (width - 15) / 2
	offY = (height - 15) / 2
	for i in range(15):
		for j in range(15):
			sensors.append(Sensor(rc, rs, moveMax, dampening, i + offX, j + offY))
	return sensors

def initSensors2(rc, rs, moveMax, dampening, width = 0, height = 0):
	sensors = []
	offX = (width - 15) / 2
	offY = (height - 15) / 2
	for i in range(15):
		for j in range(15):
			sensors.append(Sensor(rc, rs, moveMax, dampening, i + offX, j + offY))
	return sensors

def iterate(sensors):
	global grid
	moveableSensors = []
	for sensor in sensors:
		if sensor.moveCount < sensor.moveMax:
			moveableSensors.append(sensor)

	for sensor in moveableSensors:
		setDesiredMoveLocation1(sensor)

	for sensor in moveableSensors:
		setMoveLocation(sensor)

	width, height, capacity = grid["width"], grid["height"], grid.get("capacity", 1000000)
	grid = {"width":width, "height":height, "capacity": capacity}
	for sensor in sensors:
		move(sensor)


def setDesiredMoveLocation1(sensor):
	global Kcover
	def normalize(v):
		norm=np.linalg.norm(v)
		if norm==0: 
			return v
		return v/norm

	#For now distance will be max of row and column distance, later change to euclidian
	def distance(location1, location2):
		rowD = location1[0] - location2[0]
		colD = location1[1] - location2[1]
		return max(abs(rowD), abs(colD))

	"""
	gonna use modified version of the original paper, where sensors are weighted the same but no quadrants,
	so they apply a vector weight in their direction and then add up all the weights and
	choose that direction
	"""
	def calculateForce1(sensor1, sensor2, force):
		l1 = np.asarray(sensor1.currentLocation)
		l2 = np.asarray(sensor2.currentLocation)
		d = distance(sensor1.currentLocation, sensor2.currentLocation)
		weight = sensor1.rc + 1 - d
		weight *= weight
		v = l1 - l2
		v = normalize(v) * weight
		return v

	"""this works the way the paper with forces works, 
	except distance is not euclidian, and no degree force."""
	def calculateForce2(sensor1, sensor2, force):
		l1 = np.asarray(sensor1.currentLocation)
		l2 = np.asarray(sensor2.currentLocation)
		d = distance(sensor1.currentLocation, sensor2.currentLocation)
		weight = force / math.pow(d, 2)
		v = l1 - l2
		v = normalize(v) * weight
		return v

	setNeighbours(sensor)
	l1 = np.asarray(sensor.currentLocation)
	w = np.zeros(2)
	for neighbour in sensor.neighbours:
		w += calculateForce2(sensor, neighbour, Kcover)
	w += sensor.dampening * sensor.oldV
	sensor.oldV = w
	w = normalize(w)
	newV = np.zeros(2)
	if w[0] <-.5:
		newV[0] = -1
	elif w[0] <.5:
		newV[0]= 0
	else:
		newV[0] = 1
	if w[1] <-.5:
		newV[1] = -1
	elif w[1] <.5:
		newV[1] = 0
	else:
		newV[1] = 1
	newLocation =  newV + l1
	sensor.desiredMoveLocation = (newLocation[0], newLocation[1])

def setNeighbours(sensor):
	global grid
	neighbours = []
	x, y = sensor.currentLocation
	rc = sensor.rc
	for i in range(-rc, rc + 1):
		for j in range(-rc, rc + 1):
			neighbour = grid.get((i + x, j + y), [])
			neighbours.extend(neighbour)
	neighbours.remove(sensor)
	sensor.neighbours = neighbours



def setMoveLocation(sensor):
	global grid

	if sensor.conflictResolved:
		return
	if not inBounds(sensor.desiredMoveLocation):
		sensor.moveLocation = sensor.currentLocation
		sensor.conflictResolved = True
		return

	cns = findConflictNeighbours(sensor)
	cns.append(sensor)
	for cn in cns:
		cn.conflict = random.uniform(0, 1)
	sorted(cns, key = lambda x: x.conflict, reverse = True)
	if len(cns) != 1:
		print len(cns)
	capacity = grid.get("capacity", 1000000) - len(grid.get(sensor.desiredMoveLocation, []))
	i = 0
	while i < capacity and i < len(cns):
		cns[i].moveLocation = cns[i].desiredMoveLocation
		cns[i].desiredMoveLocation = None
		cns[i].conflictResolved = True
		i += 1
	while i < len(cns):
		cns[i].moveLocation = cns[i].currentLocation
		cns[i].desiredMoveLocation = None
		cns[i].conflictResolved = True
		i += 1

def inBounds(location):
	global grid
	width, height = grid["width"], grid["height"]
	if width == 0 and height == 0:
		return True
	x, y = location
	return 0<= x <= width and 0 <= y <= height

def findConflictNeighbours(sensor):
	cns = []
	for neighbour in sensor.neighbours:
		if neighbour.desiredMoveLocation == sensor.desiredMoveLocation:
			cns.append(neighbour)
	return cns

def move(sensor):
	global grid
	if sensor.moveLocation == (28,28):
		print "HEY"
	location = grid.get(sensor.moveLocation, [])
	location.append(sensor)
	grid[sensor.moveLocation] = location
	sensor.currentLocation = sensor.moveLocation
	sensor.conflict = 0
	sensor.conflictResolved = False

def main():
	test1()

if __name__ == "__main__":
	main()