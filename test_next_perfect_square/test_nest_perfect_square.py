import unittest
from next_perfect_square import find_next_square

class TestNextPerfectSquare(unittest.TestCase):

	def test_0_next_perfect_square(self):
		self.assertEqual(find_next_square(121), 144)

	def test_1_next_perfect_square(self):
		self.assertEqual(find_next_square(141), 144)

	def test_2_next_perfect_square(self):
		self.assertEqual(find_next_square(114114114), 114126489)
		
if __name__ == '__main__':
	unittest.main()