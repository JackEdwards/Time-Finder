import os

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
		if os.path.isfile("{0} values.txt".format(self.name)):
			f = open("{0} values.txt".format(self.name), 'r')
			for day in self.days:
				for hour in day.hours:
					current_line = f.readline()
					if current_line == "True\n":
						hour.available = True
					elif current_line == "False\n":
						hour.available = False

	def save(self):
		f = open("{0} values.txt".format(self.name), 'w')
		for day in self.days:
			for hour in day.hours:
				f.write("{0}\n".format(str(hour.available)))

	def update(self, choice):
		if choice == 5:
			print("Update {0}!".format(self.name))
			print("--------{0}\n".format('-' * len(self.name)))
			for day in self.days:
				for hour in day.hours:
					while True:
						answer = input("Are you available on {0}, {1}? ".format(day.name, hour.name))
						if answer == 'y':
							hour.available = True
							break
						elif answer == 'n':
							hour.available = False
							break
						else:
							print("Invalid input.")
		else:
			print("Update {0}!".format(self.name))
			print("--------{0}\n".format('-' * len(self.name)))
			for hour in self.days[choice].hours:
				while True:
					answer = input("Are you available on {0}, {1}? ".format(self.days[choice].name, hour.name))
					if answer == 'y':
						hour.available = True
						break
					elif answer == 'n':
						hour.available = False
						break
					else:
						print("Invalid input.")

		self.save()
		os.system("cls" if os.name == "nt" else "clear")
		self.display()

	def display(self):
		# Gets the amount of spaces that should be placed between the timetable name
		left_spaces = ' ' * int((83 - len(self.name)) / 2)
		right_spaces = ' ' * int((83 - len(self.name)) / 2)
		# If the name has an even amount of characters, one space is added to the right to fix formatting issues
		if len(self.name) % 2 == 0:
			right_spaces += ' '

		table_name = (
			"+-----------------------------------------------------------------------------------+\n"
			"|{0}{1}{2}|".format(left_spaces, self.name, right_spaces)
			)
		
		table_times = (
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+\n"
	 		"|   |  9.00 | 10.00 | 11.00 | 12.00 | 1.00  | 2.00  | 3.00  | 4.00  | 5.00  | 6.00  |\n"
	 		"|   | 10.00 | 11.00 | 12.00 |  1.00 | 2.00  | 3.00  | 4.00  | 5.00  | 6.00  | 7.00  |\n"
	 		"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+")

		table_days = [
			[
			"| M |",
			"| o |",
			"| n |",
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
			],
	
			[
			"| T |",
			"| u |",
			"| e |",
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
			],
	
			[
			"| W |",
			"| e |",
			"| d |",
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
			],
	
			[
			"| T |",
			"| h |",
			"| u |",
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
			],
	
			[
			"| F |",
			"| r |",
			"| i |",
			"+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+"
			]
		]
	
		empty_slot = [
			"       |",
			"       |",
			"       |",
			"-------+"
		]
	
		full_slot = [
			"#######|",
			"#######|",
			"#######|",
			"-------+"
		]
	
		for x in range(5):
			for y in range(10):
				if self.days[x].hours[y].available == True:
					table_days[x][0] += empty_slot[0]
					table_days[x][1] += empty_slot[1]
					table_days[x][2] += empty_slot[2]
				else:
					table_days[x][0] += full_slot[0]
					table_days[x][1] += full_slot[1]
					table_days[x][2] += full_slot[2]

		print(table_name)
		print(table_times)
		for day in table_days:
			for row in day:
				print(row)

		f = open("{0}.txt".format(self.name), 'w')
		f.write(table_name + '\n')
		f.write(table_times + '\n')
		for day in table_days:
			for row in day:
				f.write(row + '\n')
		input("Press enter to continue.")