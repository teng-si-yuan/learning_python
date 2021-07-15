import unittest
from adam_and_eve import create_humans

class TestAdamAndEve(unittest.TestCase):

	def test_adam(self):
		self.assertEqual(create_humans()[0].name, 'adam')

	def test_eve(self):
		self.assertEqual(create_humans()[1].name, 'eve')

if __name__ == '__main__':
	unittest.main()