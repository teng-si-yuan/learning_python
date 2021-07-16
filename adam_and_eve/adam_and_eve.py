class Human:
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

class Man(Human):
	def __init__(self, name):
		Human.__init__(self, name, 'male')

class Woman(Human):
	def __init__(self, name):
		Human.__init__(self, name, 'female')

def create_humans():
	first_humans = []
	adam = Man('adam')
	eve = Woman('eve')
	first_humans.append(adam)
	first_humans.append(eve)
	return(first_humans)

