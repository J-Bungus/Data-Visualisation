from plotly.graph_objs import Bar, Layout
from plotly import offline

from rolling_dice import Die

#Create a 6-sided die (D6)
d6 = Die()

# Make some rolls, and store results in a list
results = d6.roll(1000)

# Analyze the results
frequencies = []
for value in range(1, d6.side_count+1):
	frequencies.append(results.count(value))

# Visualize the results.
x_values = list(range(1, d6.side_count+1))
data = [Bar(x=x_values, y=frequencies)]

# Create Title and Labels
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')