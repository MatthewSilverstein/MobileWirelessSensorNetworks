""" This class will handle metrics like calculating coverage and such """

""" naive algo: add all spots to a set and count em """
def totalCoverage(grid):
	locationsCovered = set()
	print len(grid.sensorList)
	for sensor in grid.sensorList:
		rs = sensor.rs
		for x in range(-rs, rs + 1):
			for y in range(-rs, rs + 1):
				#if grid.inBoundaries((sensor.x + x, sensor.y + y)):
				locationsCovered.add((sensor.x + x, sensor.y + y))
	return len(locationsCovered)

def totalMoves(grid):
	totalMoves = 0
	for sensor in grid.sensorList:
		totalMoves += sensor.moves
	return totalMoves
