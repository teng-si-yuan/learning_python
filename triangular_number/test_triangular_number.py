import unittest
from triangular_number import triangular_number

class TestTriangularNumber(unittest.TestCase):

	def test_1_triangular_number(self):
		self.assertEqual(triangular_number(1), 1)

	def test_2_triangular_number(self):
		self.assertEqual(triangular_number(2), 3)

	def test_3_triangular_number(self):
		self.assertEqual(triangular_number(3), 6)

	def test_4_triangular_number(self):
		self.assertEqual(triangular_number(7), 28)

if __name__ == '__main__':
	unittest.main()