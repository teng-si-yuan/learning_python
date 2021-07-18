import unittest
from age_of_days import age_of_days

class TestAgeOfDays(unittest.TestCase):

	def test_common_age_of_days(self):
		self.assertEqual(age_of_days(2008, 9, 9, 2021, 7, 1), 4678)

	def test_non_change_age_of_days(self):
		self.assertEqual(age_of_days(2021, 7, 1, 2021, 7, 1), 0)

	def test_non_leap_year(self):
		self.assertEqual(age_of_days(2021, 7, 1, 2022, 7, 1), 365)

	def test_the_day_after_feb_28_to_the_day_after_feb_28(self):
		self.assertEqual(age_of_days(2020, 3, 1, 2021, 3, 1), 365)

	def test_the_day_before_feb_28_to_the_day_before_feb_28(self):
		self.assertEqual(age_of_days(2020, 1, 1, 2021, 1, 1), 366)

	def test_non_leap_year_of_100_years(self):
		self.assertEqual(age_of_days(1899, 1, 1, 1901, 1, 1), 730)

	def test_the_leap_year_of_400_years(self):
		self.assertEqual(age_of_days(1599, 7, 1, 1601, 7, 1), 731)

	def test_the_birth_month_bigger_than_now_month(self):
		self.assertEqual(age_of_days(2021, 7, 1, 2022, 6, 1), 335)

	def test_the_birth_month_smaller_than_now_month(self):
		self.assertEqual(age_of_days(2021, 6, 1, 2022, 7, 1), 395)

	def test_the_birth_day_bigger_than_now_day(self):
		self.assertEqual(age_of_days(2021, 7, 10, 2022, 7, 1), 356)

	def test_the_birth_day_smaller_than_now_day(self):
		self.assertEqual(age_of_days(2021, 7, 1, 2022, 7, 10), 374)


if __name__ == '__main__':
	unittest.main()