import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Set chart title and label axes
ax.set_title("Perfect Squares", fontsize=30)
ax.set_xlabel("Value", fontsize=18)
ax.set_ylabel("Square of Value", fontsize=18)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=15)


plt.savefig('squares_plot.png', bbox_inches='tight')
plt.savefig('perfect_squares_plot.png')
plt.show()