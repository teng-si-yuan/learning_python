import unittest
from highest_and_lowest import highest_and_lowest

class TestHighestAndLowest(unittest.TestCase):

	def test_common_highest_and_lowest1(self):
		self.assertEqual(highest_and_lowest('1 2 3 4 6'), '6 1')

	def test_common_highest_and_lowest2(self):
		self.assertEqual(highest_and_lowest('-1 1'), '1 -1')

	def test_common_highest_and_lowest3(self):
		self.assertEqual(highest_and_lowest(''), '')

	def test_common_highest_and_lowest4(self):
		self.assertEqual(highest_and_lowest('1 1'), '1 1')

	def test_common_highest_and_lowest5(self):
		self.assertEqual(highest_and_lowest('1'), '1 1')



if __name__ == '__main__':
	unittest.main()