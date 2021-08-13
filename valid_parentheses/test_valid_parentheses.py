import unittest
from valid_parentheses import validate
class TestMaximumSubarraySum(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(validate(''), True)

	def test_string_with_odd_number(self):
		self.assertEqual(validate('('), False)
		self.assertEqual(validate('()('), False)


if __name__ == '__main__':
	unittest.main()