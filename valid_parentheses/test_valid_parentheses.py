import unittest
from valid_parentheses import validate
class TestMaximumSubarraySum(unittest.TestCase):

	def test_none_maximum_subarray_sum(self):
		self.assertEqual(validate(''), True)


if __name__ == '__main__':
	unittest.main()