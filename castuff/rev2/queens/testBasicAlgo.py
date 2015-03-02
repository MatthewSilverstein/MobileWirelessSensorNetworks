from grid import Grid
from sensor import Sensor 
from metrics import totalCoverage, totalMoves
from graphs import graphCoverage, graphMoves
def test2():
	steps = 250
	rc = 4
	rs = 2
	maxMoves = 200
	grid = Grid()
	sensors = initSensors3(rc, rs, maxMoves)
	for sensor in sensors:
		grid.add(sensor)
	totalCoveragesList=[]
	totalMovesList=[]
	stepList = []
	for i in range(steps):
		changed = grid.iterate()
		print "STEP:", i
		stepList.append(i)
		totalCoveragesList.append(totalCoverage(grid))
		totalMovesList.append(totalMoves(grid))
		if not changed:
			break
	graphCoverage(stepList, totalCoveragesList)
	graphMoves(stepList, totalMovesList)
	print grid.toString()

def initSensors3(rc, rs, maxMoves):
	sensors = []
	for i in range(33):
		for j in range(33):
			sensors.append(Sensor(rc, rs, maxMoves, i, j))
	return sensors

def initSensors0(rc, rs, maxMoves):
	sensors = []
	sensors.append(Sensor(rc, rs, maxMoves,0, 0))
	sensors.append(Sensor(rc, rs, maxMoves,1, 1))
	#sensors.append(StationarySensor(rc, lowerK, upperK, -1, -1))
	#sensors.append(StationarySensor(rc, lowerK, upperK, 0, -1))
	return sensors

def initSensors1(rc, rs):
	sensors = []
	for i in range(15):
		for j in range(15):
			sensors.append(Sensor(rc, rs, i,j))
	return sensors

def initSensors2(rc, rs):
	sensors = []
	sensors.append(Sensor(rc, rs, 1, 1))
	sensors.append(Sensor(rc, rs, 1, 2))
	sensors.append(Sensor(rc, rs, 2, 1))
	sensors.append(Sensor(rc, rs, 2, 2))
	return sensors

def main():
	test2()

if __name__ == "__main__":
	main()