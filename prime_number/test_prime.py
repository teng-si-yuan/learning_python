import unittest
from prime import is_prime_number

class TestPrime(unittest.TestCase):

	def test_1_prime(self):
		self.assertEqual(is_prime_number(0), False)

	def test_2_prime(self):
		self.assertEqual(is_prime_number(1), False)

	def test_3_prime(self):
		self.assertEqual(is_prime_number(2), True)

	def test_4_prime(self):
		self.assertEqual(is_prime_number(10), False)

	def test_5_prime(self):
		self.assertEqual(is_prime_number(11), True)

if __name__ == '__main__':
	unittest.main()