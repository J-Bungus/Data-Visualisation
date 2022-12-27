import matplotlib.pyplot as plt 

from random_walk import RandomWalk

generate_plot = True

while generate_plot:
	# Make a random walk
	rw = RandomWalk(5_000)
	rw.fill_walk()

	# Plot the points in the Walk
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9))
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolors='none', s=10)
	
	# Emphasize the first and last points
	ax.scatter(0, 0, c='red', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='orange', edgecolors='none',
		s=100)

	# Set chart title and remove axes
	ax.set_title("A Random Walk")
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	#plt.savefig('random_walk.png')
	plt.show()

	# Check if another plot should be made
	keep_running = input("Make another walk? [Y/n]")

	# Continue to prompt the user until the proper input is given
	while keep_running.lower() != 'y' and keep_running != '':
		if keep_running.lower() == 'n':
			generate_plot = False
			break
		else:
			print("Invalid input.")

			keep_running = input("Make another walk? [Y/n]")