import os

from timetable import *

timetables = [ Timetable("Jack's timetable"), Timetable("Jodie's timetable") ]

def clear():
	os.system("cls" if os.name == "nt" else "clear")

def get_available_times():
	pass

def get_command():
	print("What would you like to do?\n")
	print("1. Display")
	print("2. Update")
	print("3. Quit")

	while True:
		try:
			choice = int(input("\nEnter your choice: "))
		except ValueError:
			print("\nInvalid input.")
			continue
		if choice >= 1 and choice <= 3:
			return choice
		else:
			print("\nInvalid input.")

def get_timetable():
	print("Choose a timetable.")
	for x in range(len(timetables)):
		print("{0}. {1}".format(str(x + 1), timetables[x].name))
	while True:
		try:
			choice = int(input("\nEnter your choice: "))
		except ValueError:
			print("\nInvalid input.")
			continue
		if choice >= 1 and choice <= len(timetables):
			return timetables[choice - 1]
		else:
			print("\nInvalid input.")

def get_day():
	print("Which day would you like to update?\n")
	print("1. Monday")
	print("2. Tuesday")
	print("3. Wednesday")
	print("4. Thursday")
	print("5. Friday")
	print("6. All")

	while True:
		try:
			choice = int(input("\nEnter choice: "))
		except ValueError:
			print("\nInvalid input.")
			continue
		if choice >= 1 and choice <= 6:
			clear()
			return choice - 1
		else:
			print("\nInvalid input.")

def main():
	os.system("mode con cols=86")
	for timetable in timetables:
		timetable.load()

	while True:
		clear()
		command = get_command()
		clear()

		if command == 1:
			timetable = get_timetable()
			clear()
			timetable.display()
		elif command == 2:
			timetable = get_timetable()
			clear()
			timetable.update(get_day())
		elif command == 3:
			break

if __name__ == "__main__":
	main()