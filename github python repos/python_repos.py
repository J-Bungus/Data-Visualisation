import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, additional_info = [], [], []
for repo in repo_dicts:
	repo_name = repo['name']
	repo_url = repo['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)
	stars.append(repo['stargazers_count'])

	# Additional Information
	owner = repo['owner']['login']
	description = repo['description']
	info = f"{owner} <br /> {description}"
	additional_info.append(info)

# Make visualisation
data = [{
	'type': 'bar',
	'x': repo_links,
	'y': stars,
	'hovertext': additional_info,
	'marker':{
		'color': 'rgb(170, 50, 80)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.6,
}]
my_layout = {
	'title': 'Most-Starred Python Projects on Github',
	'titlefont': {'size': 28},
	'xaxis': {
		'title': 'Repository',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
	'yaxis': {
		'title': 'Stars',
		'titlefont': {'size': 24},
		'tickfont': {'size': 14},
	},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')