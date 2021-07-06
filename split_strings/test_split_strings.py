import unittest
from split_strings import split_strings

class TestSplitStrings(unittest.TestCase):

	def test_1_split_strings(self):
		self.assertEqual(split_strings('yuan'), ['yu','an'])

	def test_2_split_strings(self):
		self.assertEqual(split_strings(''), [])

	def test_3_split_strings(self):
		self.assertEqual(split_strings('a'), ['a_'] )

	def test_4_split_strings(self):
		self.assertEqual(split_strings('hello_world'), ['he', 'll', 'o_', 'wo', 'rl', 'd_'] )

	def test_5_split_strings(self):
		self.assertEqual(split_strings('yan'), ['ya', 'n_'] )

if __name__ == '__main__':
	unittest.main()