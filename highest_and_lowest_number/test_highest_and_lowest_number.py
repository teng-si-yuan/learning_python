import unittest
from highest_and_lowest_number import highest_and_lowest_number

class TestHighestAndLowestNumber(unittest.TestCase):

	def test_0_highest_and_lowest_number(self):
		self.assertEqual(highest_and_lowest_number([]), None)

	def test_1_highest_and_lowest_number(self):
		self.assertEqual(highest_and_lowest_number([1]), (1, 1))

	def test_2_highest_and_lowest_number(self):
		self.assertEqual(highest_and_lowest_number([1, 2]), (2, 1))

	def test_16_highest_and_lowest_number(self):
		self.assertEqual(highest_and_lowest_number([2, 4, 6, 8, 10]), (10, 2))

		
if __name__ == '__main__':
	unittest.main()