import unittest
from maximum_subarray_sum import maximum_subarray_sum

class TestMaximumSubarraySum(unittest.TestCase):

	def test_none_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([]), (0, []))

	def test_one_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([1]), (1, [1]))

	def test_negative_number_maximum_subarray_sum(self):
		self.assertEqual(maximum_subarray_sum([-1, -2, -3, -4]), (0, []))

	# def test_normal_maximum_subarray_sum(self):
	# 	self.assertEqual(maximum_subarray_sum([1, 2, 3, 4]), (10, [1, 2, 3, 4]))

if __name__ == '__main__':
	unittest.main()