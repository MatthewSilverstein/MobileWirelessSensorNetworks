import unittest
from grid import Grid
from sensor import Sensor

import numpy as np
import math
kcover = 2
kdegree = 2
damp = 0.8
cdistance = 0.8

@unittest.skip("Hey")
class TestSensorFindNeighbours(unittest.TestCase):
	def setUp(self):
		pass

	def test_neighbours_zero(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
		grid.add(sensor1)
		grid.iterate()
		self.assertEqual(len(sensor1.neighbours), 0)

	def test_neighbours_one(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
		sensor2 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 1, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual(len(sensor1.neighbours), 1)

	def test_neighbours_eight_border(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
		for i in range(8):
			angle = i / 4.0 * math.pi
			x = 2.999 * math.cos(angle)
			y = 2.999 * math.sin(angle)
			print (x, y)
			sensor = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, x, y)
			grid.add(sensor)
		grid.add(sensor1)
		grid.iterate()
		self.assertEqual(len(sensor1.neighbours), 8)


class TestSensorMove(unittest.TestCase):

	def test_fcover_none(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
		grid.add(sensor1)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

	
	def test_f_direction_many(self):
		for i in range(8):
			grid = Grid()
			sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
			angle = i / 4.0 * math.pi
			x = 1 * math.cos(angle)
			y = 1 * math.sin(angle)
			grid.add(sensor1)
			sensor2 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, x, y)
			grid.add(sensor1)
			grid.add(sensor2)
			grid.iterate()
			self.assertEqual(len(sensor1.neighbours), 1)
			self.assertEqual((sensor1.v[0], sensor1.v[1]), (-x, -y))

	def test_f_cover_many(self):
		for i in range(8):
			grid = Grid()
			sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
			angle = i / 4.0 * math.pi
			x = 1 * math.cos(angle)
			y = 1 * math.sin(angle)
			grid.add(sensor1)
			sensor2 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, x, y)
			grid.add(sensor1)
			grid.add(sensor2)
			grid.iterate()
			self.assertEqual(len(sensor1.neighbours), 1)
			self.assertEqual(sensor1.fcover, -kcover)

	def test_f_cover_many(self):
		kdegree = 1
		for i in range(8):
			grid = Grid()
			sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
			angle = i / 4.0 * math.pi
			x = 1 * math.cos(angle)
			y = 1 * math.sin(angle)
			grid.add(sensor1)
			sensor2 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, x, y)
			grid.add(sensor1)
			grid.add(sensor2)
			grid.iterate()
			self.assertEqual(sensor1.critical, True)
			self.assertEqual(len(sensor1.neighbours), 1)
			self.assertEqual(sensor1.fdegree, sensor1.kdegree)

		kdegree = 0
		for i in range(8):
			grid = Grid()
			sensor1 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, 0, 0)
			angle = i / 4.0 * math.pi
			x = 1 * math.cos(angle)
			y = 1 * math.sin(angle)
			grid.add(sensor1)
			sensor2 = Sensor(3, 1, kcover, kdegree, damp, cdistance, 50, x, y)
			grid.add(sensor1)
			grid.add(sensor2)
			grid.iterate()
			self.assertEqual(sensor1.critical, False)
			self.assertEqual(len(sensor1.neighbours), 1)
			self.assertEqual(sensor1.fdegree, 0)

	def test_move_moveCount(self):
		pass

if __name__ == '__main__':
	unittest.main()