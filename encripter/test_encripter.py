import unittest
from encripter import encript

class TestSort(unittest.TestCase):

	def test_ascending_none(self):
		self.assertEqual(encript(''), '')

	def test_ascending_only_one(self):
		self.assertEqual(encript('b'), 'c')

	def test_ascending_normal_two_numbers(self):
		self.assertEqual(encript('bee'), 'cff')

if __name__ == '__main__':
	unittest.main()