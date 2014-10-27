

class Hour:
	def __init__(self, start_hour, end_hour):
		self.start_hour = start_hour
		self.end_hour = end_hour
		self.name = "{0} - {1}".format(start_hour, end_hour)
		self.available = False