import unittest
from pagination_helper import PaginationHelper

class TestPaginationHelper(unittest.TestCase):

	def test_page_count(self):
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_count(), 2)
		helper = PaginationHelper([], 4)
		self.assertEqual(helper.page_count(), 0)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 8)
		self.assertEqual(helper.page_count(), 1)

	def test_item_count(self):
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.item_count(), 6)

	def test_page_item_count(self):	
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_item_count(100), -1)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_item_count(0), 4)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_item_count(1), 2)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 8)
		self.assertEqual(helper.page_item_count(0), 6)

	def test_page_index(self):
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_index(0), 0)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_index(5), 1)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_index(10), -1)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_index(6), -1)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
		self.assertEqual(helper.page_index(-1), -1)
		helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 8)
		self.assertEqual(helper.page_index(4), 0)

if __name__ == '__main__':
	unittest.main()