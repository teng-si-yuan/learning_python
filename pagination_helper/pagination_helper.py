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

	def page(self, page_number):
		start_index = page_number * self.page_size
		page_items = []
		i = 0
		if page_number < 0:
			print("page_number < 0")
			return([])
		if page_number >= self.page_count():
			print("page_number == self.page_count()")
			return([])
		while i < 4:
			page_items.append(self.items[start_index + i])
			i = i + 1
			if start_index + i == self.item_count():
				print(i)
				break
		return(page_items)