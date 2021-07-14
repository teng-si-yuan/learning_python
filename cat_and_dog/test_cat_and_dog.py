import unittest
from cat_and_dog import cat_years, dog_years

class TestCatAndDogYears(unittest.TestCase):

	def test_0_human_year(self):
		self.assertEqual(cat_years(0), 0)
		self.assertEqual(dog_years(0), 0)

	def test_1_human_year_equals_15_cat_years_and_dog_years(self):
		self.assertEqual(cat_years(1), 15)
		self.assertEqual(dog_years(1), 15)

	def test_2_human_year_equals_24_cat_years_and_dog_years(self):
		self.assertEqual(cat_years(2), 24)
		self.assertEqual(dog_years(2), 24)

	def test_3_human_year_equals_28_cat_years_and_29_dog_years(self):
		self.assertEqual(cat_years(3), 28)
		self.assertEqual(dog_years(3), 29)


	# def test_year_2020_month_1(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 1), ['31'])

	# def test_year_2020_month_3(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 3), ['31'])

	# def test_year_2020_month_4(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 4), ['30'])

	# def test_year_2020_month_5(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 5), ['31'])

	# def test_year_2020_month_6(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 6), ['30'])

	# def test_year_2020_month_7(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 7), ['31'])

	# def test_year_2020_month_8(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 8), ['31'])

	# def test_year_2020_month_9(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 9), ['30'])

	# def test_year_2020_month_10(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 10), ['31'])

	# def test_year_2020_month_11(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 11), ['30'])

	# def test_year_2020_month_12(self):
	# 	self.assertEqual(cat_years, dog_years(2020, 12), ['31'])


if __name__ == '__main__':
	unittest.main()