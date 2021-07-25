import unittest
from sort import sort

class TestSort(unittest.TestCase):

	def test_ascending_none(self):
		self.assertEqual(sort([], True), [])

	def test_ascending_only_one(self):
		self.assertEqual(sort([1], True), [1])

	def test_ascending_normal_two_numbers(self):
		self.assertEqual(sort([2, 1], True), [1, 2])

	def test_ascending_normal_five_numbers(self):
		self.assertEqual(sort([1, 3, 2, 7, 6], True), [1, 2, 3, 6, 7])

	def test_ascending_negative_number(self):
		self.assertEqual(sort([-1, -3, 2, 7, -6], True), [-6, -3, -1, 2, 7])

	def test_descending_normal_two_numbers(self):
		self.assertEqual(sort([2, 1], False), [2, 1])

	def test_descending_normal_five_numbers(self):
		self.assertEqual(sort([1, 3, 2, 7, 6], False), [7, 6, 3, 2, 1])

	def test_descending_negative_five_numbers(self):
		self.assertEqual(sort([-1, -3, 2, 7, -6], False), [7, 2, -1, -3, -6])


if __name__ == '__main__':
	unittest.main()