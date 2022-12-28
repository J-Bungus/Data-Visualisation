import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# Extract date, and max and mintemperatures from the file
	dates, highs, lows = [], [], []
	for row in reader:
		# Get dates
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		dates.append(current_date)

		#Get temperatures
		max_temp = int(row[5])
		min_temp = int(row[6])
		highs.append(max_temp)
		lows.append(min_temp)

# Plot the high and low temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates,lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

# Format Plot
plt.title("Daily high and low temperatures - 2018 \n Sitka, AK", fontsize=30)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()