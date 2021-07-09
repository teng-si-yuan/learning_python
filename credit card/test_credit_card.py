import unittest
from credit_card_maskify import maskify

class TestCreditCard(unittest.TestCase):

	def test_0_maskify(self):
		self.assertEqual(maskify(''), '')

	def test_1_maskify(self):
		self.assertEqual(maskify('123'), '123')

	def test_2_maskify(self):
		self.assertEqual(maskify('12345'), '#2345')

	def test_16_maskify(self):
		self.assertEqual(maskify('1234567890123456'), '############3456')


if __name__ == '__main__':
	unittest.main()