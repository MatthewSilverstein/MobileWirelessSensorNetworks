""" This class will handle metrics like calculating coverage and such """

""" naive algo: add all spots to a set and count em """
def totalCoverage(grid, sensors):
	locationsCovered = set()
	for sensor in sensors:
		rs = sensor.rs
		x, y = sensor.currentLocation
		for i in range(-rs, rs + 1):
			for j in range(-rs, rs + 1):
				#if grid.inBoundaries((sensor.x + x, sensor.y + y)):
				locationsCovered.add((i + x, j + y))
	return len(locationsCovered)

def totalMoves(grid):
	totalMoves = 0
	for sensor in grid.sensorList:
		totalMoves += sensor.moves
	return totalMoves
