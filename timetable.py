from day import *

class Timetable:
	days = []

	def __init__(self):
		self.days.append(Day("Monday"))
		self.days.append(Day("Tuesday"))
		self.days.append(Day("Wednesday"))
		self.days.append(Day("Thursday"))
		self.days.append(Day("Friday"))