import unittest
from count_string import length_array

class TestCountString(unittest.TestCase):

	def test_0_length_array(self):
		self.assertEqual(length_array(''), 0)

	def test_1_length_array(self):
		self.assertEqual(length_array('yuan'), 4)

	def test_2_length_array(self):
		self.assertEqual(length_array('hello, world!'), 13)


if __name__ == '__main__':
	unittest.main()