import unittest
from grid import Grid
from sensor import Sensor
@unittest.skip("Hey")
class TestSensorMove(unittest.TestCase):

	def setUp(self):
		pass

	def test_move_none(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		grid.add(sensor1)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

	def test_move_xn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 1, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (-1, 0))

	def test_move_xp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 1, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (2, 0))

	def test_move_yn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 1)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, -1))

	def test_move_yp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 1)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (0, 2))

	def test_move_moveCount(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 0, 0, 0)
		sensor2 = Sensor(3, 1, 0, 0, 1)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

@unittest.skip("Hey")
class TestSensorBlock(unittest.TestCase):

	def setUp(self):
		pass

	def test_block_xn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 3, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

	def test_block_xp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 3, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (3, 0))

	def test_block_yn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 3)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

	def test_block_yp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 3)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (0, 3))

class TestSensorMoveBack(unittest.TestCase):

	def setUp(self):
		pass

	def test_moveBack_xn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 2, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (-1, 0))
		self.assertEqual((sensor2.x, sensor2.y), (3, 0))
		sensor1.moveBack(grid)
		self.assertEqual(sensor1.xlast, -1)
		self.assertTrue(sensor1.isEmptyX(grid, 3, -1))
		self.assertTrue(sensor1.xmoveback)
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (2, 0))

	def test_moveBack_xp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 2, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (-1, 0))
		self.assertEqual((sensor2.x, sensor2.y), (3, 0))
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

	def test_moveBack_yn(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 2)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, -1))
		self.assertEqual((sensor2.x, sensor2.y), (0, 3))
		grid.iterate()
		self.assertEqual((sensor2.x, sensor2.y), (0, 2))

	def test_moveBack_yp(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 2)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, -1))
		self.assertEqual((sensor2.x, sensor2.y), (0, 3))
		grid.iterate()
		self.assertEqual((sensor1.x, sensor1.y), (0, 0))

@unittest.skip("Hey")
class TestSensorFunctions(unittest.TestCase):

	def setUp(self):
		pass

	def test_count_basic(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		grid.add(sensor1)
		self.assertEqual(sensor1.countSensors(grid, -3, -3, 6, 6), 1)

	def test_count_sameLocation(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertEqual(sensor1.countSensors(grid, -3, -3, 6, 6), 2)

	def test_count_boundaries(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 3, 3)
		sensor3 = Sensor(3, 1, 50, -3, -3)
		sensor4 = Sensor(3, 1, 50, -3, 3)
		sensor5 = Sensor(3, 1, 50, 3, -3)
		grid.add(sensor1)
		grid.add(sensor2)
		grid.add(sensor3)
		grid.add(sensor4)
		grid.add(sensor5)
		self.assertEqual(sensor1.countSensors(grid, -3, -3, 6, 6), 5)

	def test_isEmptyX_n_notempty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 2, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertFalse(sensor2.isEmptyX(grid, 2, 1))

	def test_isEmptyX_n_empty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 3, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertTrue(sensor2.isEmptyX(grid, 2, 1))

	def test_isEmptyX_p_notempty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 2, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertFalse(sensor1.isEmptyX(grid, 2, -1))

	def test_isEmptyX_p_empty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 3, 0)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertTrue(sensor1.isEmptyX(grid, 2, -1))

	def test_isEmptyY_n_notempty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 2)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertFalse(sensor2.isEmptyY(grid, 2, 1))

	def test_isEmptyY_n_empty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 3)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertTrue(sensor2.isEmptyY(grid, 2, 1))

	def test_isEmptyY_p_notempty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 2)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertFalse(sensor1.isEmptyY(grid, 2, -1))

	def test_isEmptyY_p_empty(self):
		grid = Grid()
		sensor1 = Sensor(3, 1, 50, 0, 0)
		sensor2 = Sensor(3, 1, 50, 0, 3)
		grid.add(sensor1)
		grid.add(sensor2)
		self.assertTrue(sensor1.isEmptyY(grid, 2, -1))		

if __name__ == '__main__':
	unittest.main()