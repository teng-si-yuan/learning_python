import unittest
from welcome import welcome

class TestWelcome(unittest.TestCase):

	def test_english(self):
		self.assertEqual(welcome("english"), "welcome")

	def test_french(self):
		self.assertEqual(welcome("french"), "bienvenue")

if __name__ == '__main__':
	unittest.main()