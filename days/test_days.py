import unittest
from days import days

class TestDays(unittest.TestCase):

	def test_year_0_month_2(self):
		self.assertEqual(days(0, 2), [])

	def test_year_1_month_2(self):
		self.assertEqual(days(1, 2), ['29'])

	def test_year_1000_month_2(self):
		self.assertEqual(days(1000, 2), ['28'])

	def test_year_2020_month_2(self):
		self.assertEqual(days(2020, 2), ['29'])

	def test_year_2020_month_1(self):
		self.assertEqual(days(2020, 1), ['31'])

	def test_year_2020_month_3(self):
		self.assertEqual(days(2020, 3), ['31'])

	def test_year_2020_month_4(self):
		self.assertEqual(days(2020, 4), ['30'])

	def test_year_2020_month_5(self):
		self.assertEqual(days(2020, 5), ['31'])

	def test_year_2020_month_6(self):
		self.assertEqual(days(2020, 6), ['30'])

	def test_year_2020_month_7(self):
		self.assertEqual(days(2020, 7), ['31'])

	def test_year_2020_month_8(self):
		self.assertEqual(days(2020, 8), ['31'])

	def test_year_2020_month_9(self):
		self.assertEqual(days(2020, 9), ['30'])

	def test_year_2020_month_10(self):
		self.assertEqual(days(2020, 10), ['31'])

	def test_year_2020_month_11(self):
		self.assertEqual(days(2020, 11), ['30'])

	def test_year_2020_month_12(self):
		self.assertEqual(days(2020, 12), ['31'])


if __name__ == '__main__':
	unittest.main()