import unittest
from prime_factors import prime_factors

class Testprime_factors(unittest.TestCase):

	def test_0_prime_factors(self):
		self.assertEqual(prime_factors(0), [])

	def test_1_prime_factors(self):
		self.assertEqual(prime_factors(1), [])

	def test_2_prime_factors(self):
		self.assertEqual(prime_factors(2), [])

	def test_3_prime_factors(self):
		self.assertEqual(prime_factors(3), [])

	def test_4_prime_factors(self):
		self.assertEqual(prime_factors(4), [1, 2, 4])

	def test_16_prime_factors(self):
		self.assertEqual(prime_factors(16),[1, 2, 4, 8, 16])
if __name__ == '__main__':
	unittest.main()