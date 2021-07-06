import unittest
from remove_array import remove_array

class TestRemoveArray(unittest.TestCase):

	def test_1_remove_array(self):
		self.assertEqual(remove_array(['apple', 'banana', 'cherry'], 'banana'), ['apple', 'cherry'])

	def test_2_remove_array(self):
		self.assertEqual(remove_array([''], 'banana'), [''])

	def test_3_remove_array(self):
		self.assertEqual(remove_array(['apple', 'cherry'], 'banana'), ['apple', 'cherry'] )

if __name__ == '__main__':
	unittest.main()