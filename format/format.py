class HTMLFormat:
	def __init__(self):
		pass

	def div(self, text):
		return('<div>') + text + ('</div>')

	def p(self, text):
		return('<p>') + text + ('</p>')

	def span(self, text):
		return('<span>') + text + ('</span>')

	def h1(self, text):
		return('<h1>') + text + ('</h1>')	