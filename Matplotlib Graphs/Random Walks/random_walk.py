from random import choice

class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self, num_points=5000):
		"""initialize attributes of a walk"""
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		step_direction = choice([1, -1])
		fib = [0, 1]
		for i in range(2, 13):
			fib.append(fib[i-1] + fib[i-2])
		step_distance = choice(fib)
		step = step_direction * step_distance

		return step

	def fill_walk(self):
		"""calculate all the points in the walk"""

		# Keep taking steps until the walk reaches the desired length (5000)
		while len(self.x_values) < self.num_points:

			# Decide which direction to go and how far to go in that direction
			x_step = self.get_step()
			y_step = self.get_step()

			# Reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)