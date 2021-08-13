import unittest
from valid_parentheses import validate
class TestValidParentheses(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(validate(''), True)

	def test_string_with_odd_number(self):
		self.assertEqual(validate('('), False)
		self.assertEqual(validate('()('), False)

	def test_invalid_string(self):
 		self.assertEqual(validate('()(('), False)
 		self.assertEqual(validate(')(()))'), False)
 		self.assertEqual(validate(')('), False)

	def test_valid(self):
		self.assertEqual(validate('()'), True)
		self.assertEqual(validate('(())((()())())'), True)


if __name__ == '__main__':
	unittest.main()