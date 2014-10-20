import os

from timetable import *

timetables = [ Timetable("Jack's timetable"), Timetable("Jodie's timetable") ]

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
	print("3. Quit")

	while True:
		choice = input("\nEnter your choice: ")
		if choice == '1':
			return choice
		elif choice == '2':
			return choice
		elif choice == '3':
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
			break

if __name__ == "__main__":
	main()