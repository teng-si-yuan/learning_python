import unittest
from adam_and_eve import create_humans

class TestAdamAndEve(unittest.TestCase):

	def test_adam1(self):
		self.assertEqual(create_humans()[0].name, 'adam')

	def test_eve1(self):
		self.assertEqual(create_humans()[1].name, 'eve')

	def test_adam2(self):
		self.assertEqual(create_humans()[0].sex, 'male')

	def test_eve2(self):
		self.assertEqual(create_humans()[1].sex, 'female')

if __name__ == '__main__':
	unittest.main()