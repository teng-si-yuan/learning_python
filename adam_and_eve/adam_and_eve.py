class Human:
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

def create_humans():
	first_humans = []
	adam = Human('adam', 'male')
	eve = Human('eve', 'female')
	first_humans.append(adam)
	first_humans.append(eve)
	return(first_humans)
