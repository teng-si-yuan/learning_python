import math
class PaginationHelper:
	def __init__(self, items, page_size):
		self.items = items
		self.page_size = page_size

	def page_count(self):
		return(math.ceil(len(self.items) / self.page_size))

	def item_count(self):
		return(len(self.items))

	def page_item_count(self, page):
		if (page + 1 > self.page_count()):
			return(-1)
		if (page + 1 < self.page_count()):
			return(self.page_size)
		if (page + 1 == self.page_count()):
			return(len(self.items) % self.page_size)

	def page_index(self, item_index):
		if item_index < len(self.items):
			x = item_index / self.page_size
			return(math.floor(x))
		if item_index >= len(self.items):
			return(-1)
		if item_index < 0:
			return(-1)