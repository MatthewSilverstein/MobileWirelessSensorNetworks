from grid import Grid
from sensor import Sensor, StationarySensor
from metrics import totalCoverage, totalMoves
from graphs import graphCoverage, graphMoves
def test2():
	width = 39
	height = 39
	steps = 700
	rc = 4
	rs = 1
	maxMoves = 100
	lowerK = 5
	upperK = 1
	capacity = 1
	grid = Grid(width, height, capacity)
	sensors = initSensors3(rc, rs, maxMoves, lowerK, upperK, width, height)
	for sensor in sensors:
		grid.add(sensor)
	totalCoveragesList=[]
	totalMovesList=[]
	stepList = []
	for i in range(steps):
		changed = grid.iterate(i)
		print "STEP:", i
		if i % 1 == 0:
			stepList.append(i / 2)
			totalCoveragesList.append(totalCoverage(grid))
			totalMovesList.append(totalMoves(grid))
		if not changed:
			break
	graphCoverage(stepList, totalCoveragesList)
	graphMoves(stepList, totalMovesList)
	print grid.toString()

def initSensors3(rc, rs, maxMoves, lowerK, upperK, width, height):
	sensors = []
	offX = (width - 15) / 2
	offY = (height - 15) / 2
	for i in range(15):
		for j in range(15):
			sensors.append(Sensor(rc, rs, maxMoves, lowerK, upperK, i + offX, j + offY))
	return sensors

def test1():
	width = 14
	height = 14
	steps = 300
	rc = 4
	lowerK = 5
	upperK = 1
	grid = Grid(width, height, 1)
	sensors = initSensors2(rc, lowerK, upperK)
	for sensor in sensors:
		grid.add(sensor)
	for i in range(steps):
		changed = grid.iterate(i)
		print "STEP:",i
		if not changed:
			break
	print grid.toString()

def test0():
	steps = 2
	rc = 4
	lowerK = 5
	upperK = 1
	capacity = 0
	grid = Grid(capacity=capacity)
	sensors = initSensors0(rc, lowerK, upperK)
	guy = sensors[0]
	for sensor in sensors:
		grid.add(sensor)
	for i in range(steps):
		changed = grid.iterate(i)
		print "STEP:",i
		print guy.Q1, guy.Q2, guy.Q3, guy.Q4
		print guy.minQ, guy.maxQ
		print guy.moveLocation
		print "L: ",guy.x, guy.y
		print grid.toString()
		if not changed:
			break

def initSensors0(rc, lowerK, upperK):
	sensors = []
	sensors.append(Sensor(rc, lowerK, upperK, 0, 0))
	#sensors.append(StationarySensor(rc, lowerK, upperK, -1, -1))
	#sensors.append(StationarySensor(rc, lowerK, upperK, 0, -1))
	sensors.append(StationarySensor(rc, lowerK, upperK, -1, 0))
	sensors.append(StationarySensor(rc, lowerK, upperK, -1, 1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 0, 1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, -1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, 0))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, 1))
	return sensors

def initSensors1(rc, lowerK, upperK):
	sensors = []
	for i in range(15):
		for j in range(15):
			sensors.append(Sensor(rc, lowerK, upperK, i,j))
	return sensors

def initSensors2(rc, lowerK, upperK):
	sensors = []
	sensors.append(Sensor(rc, lowerK, upperK, 1, 1))
	sensors.append(Sensor(rc, lowerK, upperK, 1, 2))
	sensors.append(Sensor(rc, lowerK, upperK, 2, 1))
	sensors.append(Sensor(rc, lowerK, upperK, 2, 2))
	return sensors

def main():
	test2()

if __name__ == "__main__":
	main()