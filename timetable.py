import os.path
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

	def load(self):
		f = open("{0}.txt".format(self.name), 'r')
		for day in self.days:
			for hour in day.hours:
				current_line = f.readline()
				if current_line == "True\n":
					hour.available = True
				elif current_line == "False\n":
					hour.available = False

	def save(self):
		f = open("{0}.txt".format(self.name), 'w')

		for day in self.days:
			for hour in day.hours:
				f.write("{0}\n".format(str(hour.available)))


	def update(self):
		print("Update {0}!".format(self.name))
		print("--------{0}\n".format('-' * len(self.name)))
		for day in self.days:
			for hour in day.hours:
				while True:
					answer = input("Are you available on {0} from {1}? Y/N: ".format(day.name, hour.name)).lower()
					if answer == 'y':
						hour.available = True
						break
					elif answer == 'n':
						hour.available = False
						break
					else:
						print("Invalid input.")
		self.save()

	def display(self):
		print(self.name)
		print('-' * len(self.name) + '\n')
		for day in self.days:
			for hour in day.hours:
				print("{0} from {1}: {2}".format(day.name, hour.name, hour.available))
			print()
		input("Press enter to continue.")