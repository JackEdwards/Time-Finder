from hour import *

class Day:

	def __init__(self, name):
		self.name = name
		self.hours = []
		self.hours.append(Hour("9 - 10"))
		self.hours.append(Hour("10 - 11"))
		self.hours.append(Hour("11 - 12"))
		self.hours.append(Hour("12 - 1"))
		self.hours.append(Hour("1 - 2"))
		self.hours.append(Hour("2 - 3"))
		self.hours.append(Hour("3 - 4"))
		self.hours.append(Hour("4 - 5"))
		self.hours.append(Hour("5 - 6"))