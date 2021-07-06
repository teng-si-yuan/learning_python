import unittest
from lengtharray import length_array

class TestLengthArray(unittest.TestCase):

	def test_empty_length_array(self):
		self.assertEqual(length_array([]), 0)

	def test_normal_length_array(self):
		self.assertEqual(length_array([1, 2, 3]), 3)

	def test_string_length_array(self):
		self.assertEqual(length_array(['1', '2', '3']), 3)
		
if __name__ == '__main__':
	unittest.main()