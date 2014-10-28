import os

class GraphicalTimetable:
	def __init__(self):
		pass

	def display(self, temp):
		top = ("+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+\n"
	  	   "|   |  9.00 | 10.00 | 11.00 | 12.00 | 1.00  | 2.00  | 3.00  | 4.00  | 5.00  | 6.00  |\n"
	  	   "|   | 10.00 | 11.00 | 12.00 |  1.00 | 2.00  | 3.00  | 4.00  | 5.00  | 6.00  | 7.00  |\n"
	  	   "+---+-------+-------+-------+-------+-------+-------+-------+-------+-------+-------+")

		days = [
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

		os.system("mode con cols=87")

		available_timeslots = []
		for x in range(5):
			available_timeslots.append(['', '', '', '', '', '', '', '', '', ''])

		z = 0
		for x in range(5):
			for y in range(10):
				available_timeslots[x][y] = temp[z]
				z += 1

		for x in range(5):
			for y in range(10):
				if available_timeslots[x][y].available == True:
					days[x][0] += empty_slot[0]
					days[x][1] += empty_slot[1]
					days[x][2] += empty_slot[2]
				else:
					days[x][0] += full_slot[0]
					days[x][1] += full_slot[1]
					days[x][2] += full_slot[2]
		
		print(top)
		for day in days:
			for row in day:
				print(row)

		f = open("available-timeslots.txt", 'w')
		f.write(top + '\n')
		for day in days:
			for row in day:
				f.write(row + '\n')

		input("Press enter to continue.")