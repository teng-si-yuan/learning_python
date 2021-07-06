import unittest
from triangular_number_array import triangular_number_array

class TestTriangularNumber(unittest.TestCase):

	def test_1_triangular_number_array(self):
		self.assertEqual(triangular_number_array(1), [1])

	def test_2_triangular_number_array(self):
		self.assertEqual(triangular_number_array(2), [2,3])

	def test_3_triangular_number_array(self):
		self.assertEqual(triangular_number_array(3), [4, 5, 6])

if __name__ == '__main__':
	unittest.main()