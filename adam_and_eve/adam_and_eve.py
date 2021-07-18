class Human:
	def __init__(self, name, sex):
		self.name = name
		self.sex = sex

	def say_hi(self):
		print("Hello my name is " + self.name)


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
	adam.say_hi()
	eve.say_hi()
	return(first_humans)

create_humans()

