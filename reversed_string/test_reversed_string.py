import unittest
from reversed_string import reversed_string

class TestRerversedString(unittest.TestCase):

	def test_1_reversed_string(self):
		self.assertEqual(reversed_string('wo'), 'ow')

	def test_2_reversed_string(self):
		self.assertEqual(reversed_string(''), '')

	def test_3_reversed_string(self):
		self.assertEqual(reversed_string('w'), 'w' )

	def test_5_reversed_string(self):
		self.assertEqual(reversed_string('world'), 'dlrow' )

if __name__ == '__main__':
	unittest.main()