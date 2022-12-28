import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
	all_eq_data = json.load(f)

# Loading earthquake data into a list
all_eq_dicts = all_eq_data['features']

# Extracting longitude, latitude, magnitudes, and additional information
lons, lats, mags, additional_info = [], [], [], []
for eq_dict in all_eq_dicts:
	lons.append(eq_dict['geometry']['coordinates'][0])
	lats.append(eq_dict['geometry']['coordinates'][1])
	mags.append(eq_dict['properties']['mag'])
	additional_info.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': additional_info,

	# Make markers colourful
	'marker': {
		'size': [5*mag for mag in mags],
		'color': mags,
		'colorscale': 'Jet',
		'colorbar': {'title': 'Magnitude'}
	},
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')