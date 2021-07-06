import unittest
from prime_zhi_yin_zi import prime_zhi_yin_zi

class Testprime_zhi_yin_zi(unittest.TestCase):

	def test_0_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(0), [])

	def test_1_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(1), [])

	def test_2_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(2), [2])

	def test_3_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(3), [3])

	def test_4_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(4), [2])

	def test_16_prime_zhi_yin_zi(self):
		self.assertEqual(prime_zhi_yin_zi(16),[2])
		
if __name__ == '__main__':
	unittest.main()