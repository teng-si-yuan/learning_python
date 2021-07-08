import unittest
from Fibonacci_sequence import fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):

	def test_0_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(0), [])

	def test_1_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(1), [0])

	def test_2_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(2), [0, 1])

	def test_3_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(3), [0, 1, 1])

	def test_4_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(4), [0, 1, 1, 2])

	def test_10_fibonacci_sequence(self):
		self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == '__main__':
	unittest.main()