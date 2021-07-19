import unittest
from highest_and_lowest import highest_and_lowest

class TestHighestAndLowest(unittest.TestCase):

	def test_common_numbers_highest_and_lowest(self):
		self.assertEqual(highest_and_lowest('1 2 3 4 6'), '6 1')

	def test_minus_numbers_highest_and_lowest(self):
		self.assertEqual(highest_and_lowest('-1 1'), '1 -1')

	def test_empty_number_highest_and_lowest(self):
		self.assertEqual(highest_and_lowest(''), '')

	def test_same_numbers_highest_and_lowest(self):
		self.assertEqual(highest_and_lowest('1 1'), '1 1')

	def test_only_one_number_highest_and_lowest(self):
		self.assertEqual(highest_and_lowest('1'), '1 1')

if __name__ == '__main__':
	unittest.main()