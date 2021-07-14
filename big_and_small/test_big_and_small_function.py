import unittest
from big_and_small_function import split_array

class TestBigAndSmallNumber(unittest.TestCase):

	def test_array_of_empty(self):
		self.assertEqual(split_array([], 99), ([], []))

	def test_array_of_small_number(self):
		self.assertEqual(split_array([1], 99), ([], [1]))

	def test_array_of_big_number(self):
		self.assertEqual(split_array([100], 99), ([100], []))

	def test_array_of_normal(self):
		self.assertEqual(split_array([15,23,17,4,135], 99), ([135], [15, 23, 17, 4]))


if __name__ == '__main__':
	unittest.main()