import os

from timetable import *
from timeslot import *
from graphical_timetable import *

timetables = [ Timetable("Jack's timetable"), Timetable("Jodie's timetable") ]
graphical_timetable = GraphicalTimetable()
available_timeslots = []

def get_timeslots():
	jack_timeslots = []
	jodie_timeslots = []

	# Creates a list of timeslots for each timetable
	for day in timetables[0].days:
		for hour in day.hours:
			jack_timeslots.append(Timeslot(day.name, hour.start_hour, hour.end_hour, hour.available))
	for day in timetables[1].days:
		for hour in day.hours:
			jodie_timeslots.append(Timeslot(day.name, hour.start_hour, hour.end_hour, hour.available))

	# Uses the two lists to create a new list of available timeslots
	for x in range(50):
		if jack_timeslots[x].available == True and jodie_timeslots[x].available == True:
			available_timeslots.append(Timeslot(jack_timeslots[x].day_name, jack_timeslots[x].start_hour, jack_timeslots[x].end_hour, True))
		else:
			available_timeslots.append(Timeslot(jack_timeslots[x].day_name, jack_timeslots[x].start_hour, jack_timeslots[x].end_hour, False))

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def get_timetable():
	print("Choose a timetable.")
	print("1. {0}".format(timetables[0].name))
	print("2. {0}".format(timetables[1].name))
	while True:
		choice = input("\nEnter your choice: ")
		if choice == '1':
			return timetables[0]
		elif choice == '2':
			return timetables[1]
		else:
			print("Invalid input.")

def get_command():
	print("What would you like to do?\n")
	print("1. Display")
	print("2. Update")
	print("3. Display graphical timetable")
	print("4. Quit")

	while True:
		choice = input("\nEnter your choice: ")
		if choice == '1':
			return choice
		elif choice == '2':
			return choice
		elif choice == '3':
			return choice
		elif choice == '4':
			return choice
		else:
			print("Invalid input.")

def main():
	timetables[0].load()
	timetables[1].load()

	while True:
		clear()
		command = get_command()
		clear()

		if command == '1':
			timetable = get_timetable()
			clear()
			timetable.display()
		elif command == '2':
			timetable = get_timetable()
			clear()
			timetable.update()
		elif command == '3':
			get_timeslots()
			graphical_timetable.display(available_timeslots)
		elif command == '4':
			break

if __name__ == "__main__":
	main()