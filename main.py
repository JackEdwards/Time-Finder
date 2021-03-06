import os

from timetable import *

timetables = [
	DynamicTimetable("Jack's timetable"),
	DynamicTimetable("Jodie's timetable"),
	StaticTimetable("Both available")
]

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

def get_timetable(only_dynamic):
	print("Choose a timetable.")

	if not only_dynamic:
		for x in range(len(timetables)):
			print("{0}. {1}".format(str(x + 1), timetables[x].name))
		print("{0}. Back".format(str(len(timetables) + 1)))
		while True:
			try:
				choice = int(input("\nEnter your choice: "))
			except ValueError:
				print("\nInvalid input.")
				continue
			if choice >= 1 and choice <= len(timetables):
				return timetables[choice - 1]
			elif choice == len(timetables) + 1:
				return None
			else:
				print("\nInvalid input.")

	if only_dynamic:
		dynamic_timetables = []
		for timetable in timetables:
			if type(timetable) is DynamicTimetable:
				dynamic_timetables.append(timetable)
	
		for x in range(len(dynamic_timetables)):
			print("{0}. {1}".format(str(x + 1), dynamic_timetables[x].name))
		print("{0}. Back".format(str(len(dynamic_timetables) + 1)))
		while True:
			try:
				choice = int(input("\nEnter your choice: "))
			except ValueError:
				print("\nInvalid input.")
				continue
			if choice >= 1 and choice <= len(dynamic_timetables):
				return dynamic_timetables[choice - 1]
			elif choice == len(dynamic_timetables) + 1:
				return None
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
	print("7. Back")

	while True:
		try:
			choice = int(input("\nEnter choice: "))
		except ValueError:
			print("\nInvalid input.")
			continue
		if choice >= 1 and choice <= 6:
			clear()
			return choice - 1
		elif choice == 7:
			return None
		else:
			print("\nInvalid input.")

def main():
	os.system("mode con cols=86 lines=60")
	for timetable in timetables:
		timetable.load()

	while True:
		timetables[2].update(timetables[0], timetables[1])
		clear()
		command = get_command()
		clear()

		# Display
		if command == 1:
			timetable = get_timetable(False)
			if timetable == None:
				continue
			clear()
			timetable.display()

		# Update
		elif command == 2:
			timetable = get_timetable(True)
			if timetable == None:
				continue
			clear()
			choice = get_day()
			if choice == None:
				continue
			timetable.update(choice)

		# Quit
		elif command == 3:
			break

if __name__ == "__main__":
	main()