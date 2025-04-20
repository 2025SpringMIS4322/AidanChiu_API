import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #THIS IS API ENDPOINT
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # Response object (JSON object)
print(f"Status code: {r.status_code}")

# Create an output file so we can see the JSON response that was 
# returned by the API call
outfile = open('output.json', 'w')


response = r.json() # Create a python object called 'response'

json.dump(response,outfile,indent=4) # dump() takes stuff returned from API call (dictionary) and puts in into a new outfile with indent

list_of_repos = response['items'] # Create a list of repositories

# Print out # of repos returned from API call
print(len(list_of_repos))

# Examine first repo
first_repo = list_of_repos[0] # first element of list (first dictionary/first repository)

# Find # of keys in each repo
print(f"Number of keys: {len(first_repo)}")

# print out each key
for key in first_repo:
    print(key)

# EXERCISES

# 1. Print out full name, html url, license name, and topics for first repo

print(f"Full Name: {first_repo['full_name']}") # full name
print(f"html url: {first_repo['owner']['html_url']}") # html url
print(f"License Name: {first_repo['license']['name']}") # license name

for topic in first_repo['topics']: # this is a list object
    print(f"Topic Name: {topic}")


# 2. Grab the Top 10 repos based on STAR COUNT and represent them on a bar chart

from plotly.graph_objs import Bar 
from plotly import offline

repo_names, stars = [], [] # Create multiple objects of same type

# slice list for top 10 gathering
for repo_dict in list_of_repos[:10]:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count']) # plotting on bar graph requires list of the two items

data = [
    {
        "type":"bar",
        "x":repo_names,
        "y":stars,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width":1.5, "color": "rgb(25,25,25)"},
        },
        "opacity":0.6
    }
]

my_layout = {
    "title":"Most Starred Python Repositories on GitHub",
    "xaxis":{"title":"Repository"},
    "yaxis":{"title":"Stars"},
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig, filename="python_repos.html")