

class Timeslot:
	def __init__(self, day_name, start_hour, end_hour, available):
		self.day_name = day_name
		self.start_hour = start_hour
		self.end_hour = end_hour
		self.start_period = "am" if int(start_hour) >= 9 and int(start_hour) <= 11 else "pm"
		self.end_period = "am" if int(end_hour) >= 9 and int(start_hour) <= 11 else "pm"
		self.available = available