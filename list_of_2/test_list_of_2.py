import unittest
from list_of_2 import list_of_2

class TestListOf2(unittest.TestCase):

	def test_0_list_of_2(self):
		self.assertEqual(list_of_2(0), [])

	def test_1_normal_list_of_2(self):
		self.assertEqual(list_of_2(1), [])

	def test_2_string_list_of_2(self):
		self.assertEqual(list_of_2(2), [2])

	def test_16_string_list_of_2(self):
		self.assertEqual(list_of_2(16), [2, 4, 8, 16])

	def test_18_string_list_of_2(self):
		self.assertEqual(list_of_2(80000), [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536])

		
if __name__ == '__main__':
	unittest.main()