import unittest
from sort import sort

class TestSort(unittest.TestCase):

	def test_none(self):
		self.assertEqual(sort([]), [])

	def test_only_one(self):
		self.assertEqual(sort([1]), [1])

	def test_normal_two_numbers(self):
		self.assertEqual(sort([2, 1]), [1, 2])

	def test_normal_five_numbers(self):
		self.assertEqual(sort([1, 3, 2, 7, 6]), [1, 2, 3, 6, 7])

	def test_negative_number(self):
		self.assertEqual(sort([-1, -3, 2, 7, -6]), [-6, -3, -1, 2, 7])


if __name__ == '__main__':
	unittest.main()