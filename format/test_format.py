import unittest
from format import HTMLFormat

class TestFormat(unittest.TestCase):

	def test_div(self):
		format = HTMLFormat()
		self.assertEqual(format.div('foo'), '<div>foo</div>')

	def test_p(self):
		format = HTMLFormat()
		self.assertEqual(format.p('bar'), '<p>bar</p>')

	def test_span(self):
		format = HTMLFormat()
		self.assertEqual(format.span('fiz'), '<span>fiz</span>')

	def test_h1(self):
		format = HTMLFormat()
		self.assertEqual(format.h1('buz'), '<h1>buz</h1>')


if __name__ == '__main__':
	unittest.main()