from day import *

class Timetable:
	def __init__(self, name):
		self.name = name
		self.days = []
		self.days.append(Day("Monday"))
		self.days.append(Day("Tuesday"))
		self.days.append(Day("Wednesday"))
		self.days.append(Day("Thursday"))
		self.days.append(Day("Friday"))

	def update(self):
		print("Update {0}!".format(self.name))
		print("--------" + '-' * len(self.name))
		for day in self.days:
			for hour in day.hours:
				answer = input("Are you available on {0} from {1}? Y/N: ".format(day.name, hour.name)).lower()
				if answer == 'y':
					hour.available = True

	def display(self):
		for day in self.days:
			for hour in day.hours:
				print("{0} from {1}: {2}".format(day.name, hour.name, hour.available))