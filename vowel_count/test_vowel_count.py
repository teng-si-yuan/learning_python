import unittest
from vowel_count import vowel_count

class TestVowelCount(unittest.TestCase):

	def test_vowel_not_exist(self):
		self.assertEqual(vowel_count("glksh"), 0)

	def test_vowel_only(self):
		self.assertEqual(vowel_count("aeiou"), 5)

	def test_both_vowel_and_not_vowel(self):
		self.assertEqual(vowel_count("genaimi is so fat"), 7)

if __name__ == '__main__':
	unittest.main()