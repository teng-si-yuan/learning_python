import unittest
from maximum_subarray_sum import maximum_subarray_sum

class TestMaximumSubarraySum(unittest.TestCase):

	def test_none_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([]), (0, []))

	def test_one_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([1]), (1, [1]))

	def test_positive_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([1, 2, 3, 4]), (10, [1, 2, 3, 4]))

	def test_negative_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([-1, -2, -3, -4]), (0, []))

	def test_both_positive_negative_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([4, -1, 2, -3]), (5, [4, -1, 2]))

	# def test_both_positive_negative_number_maximum_subarray_sum(self):
	# 	self.assertEqual(maximum_subarray_sum([-1, 2, -3, 4]), (4, [4]))

if __name__ == '__main__':
	unittest.main()