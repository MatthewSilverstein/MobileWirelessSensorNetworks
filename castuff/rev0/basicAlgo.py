from grid import Grid, UBGrid

from sensor import Sensor, StationarySensor



def initSensors1():
	sensors = []
	rc = 4
	lowerK = 1
	upperK = 5
	for i in range(3):
		for j in range(3):
			sensors.append(Sensor(rc, lowerK, upperK, i,j))
	return sensors

def initSensors2():
	sensors = []
	rc = 4
	lowerK = 0
	upperK = 5
	sensors.append(Sensor(rc, lowerK, upperK, 0, 0))
	sensors.append(StationarySensor(rc, lowerK, upperK, -1, -1))
	sensors.append(StationarySensor(rc, lowerK, upperK, -1, 0))
	sensors.append(StationarySensor(rc, lowerK, upperK, -1, 1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 0, -1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 0, 1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, -1))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, 0))
	sensors.append(StationarySensor(rc, lowerK, upperK, 1, 1))
	return sensors

def main():
	width = 100
	height = 100
	steps = 100
	grid = UBGrid()
	sensors = initSensors1()
	for sensor in sensors:
		grid.add(sensor)
	guy = sensors[0]
	for i in range(100):
		changed = grid.iterate(i)
		print "STEP:",i
		print grid.toString()
		if not changed:
			break


if __name__ == "__main__":
	main()