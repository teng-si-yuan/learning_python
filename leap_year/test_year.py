import unittest
from year import is_leap_year

class TestLeapYear(unittest.TestCase):

	def test_normal_leap_year(self):
		self.assertTrue(is_leap_year(2020))

	def test_hundred_year(self):
		self.assertFalse(is_leap_year(2100))

	def test_non_leap_year(self):
		self.assertFalse(is_leap_year(2101))

	def test_four_hundred_year(self):
		self.assertTrue(is_leap_year(2400))

if __name__ == '__main__':
	unittest.main()