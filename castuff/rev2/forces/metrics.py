""" This class will handle metrics like calculating coverage and such """

""" naive algo: add all spots to a set and count em """
def totalCoverage(grid):
	locationsCovered = set()
	for sensor in grid.sensorList:
		rs = sensor.rs
		x, y = sensor.x, sensor.y
		for i in range(-rs, rs + 1):
			for j in range(-rs, rs + 1):
				#if grid.inBoundaries((sensor.x + x, sensor.y + y)):
				locationsCovered.add((i + x, j + y))
	return len(locationsCovered)

def totalMoves(grid):
	totalMoves = 0
	for sensor in grid.sensorList:
		totalMoves += sensor.moveCount
	return totalMoves
