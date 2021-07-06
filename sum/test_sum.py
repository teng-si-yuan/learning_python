import unittest
from sum import sum

class TestSum(unittest.TestCase):

	def test_1_sum(self):
		self.assertEqual(sum(''), ['yu','an'])

	def test_2_sum(self):
		self.assertEqual(sum(10), 55)

	def test_3_sum(self):
		self.assertEqual(sum(100), 5050 )

if __name__ == '__main__':
	unittest.main()