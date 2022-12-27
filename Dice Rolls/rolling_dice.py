from random import randint

class Die:
	"""A class representing a single die"""

	def __init__(self, side_count=6):
		"""Set default to be a 6-sided die"""
		self.side_count = side_count

	def roll (self, num_times=1):
		"""
		Return the values rolled based on the number of times its
		rolled and number of sides the die has
		"""
		rolls = []
		for i in range(num_times):
			rolls.append(randint(1, self.side_count))

		return rolls