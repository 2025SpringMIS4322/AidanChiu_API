import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')
submission_ids = r.json() # use .json() to convert 'r' into python object

json.dump(submission_ids, outfile, indent=3)

# Make another call to an API to get specific details for a story
url = 'https://hacker-news.firebaseio.com/v0/item/43614285.json' # Create a URL
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile, indent=4)

# EXERCISE
# 3. Grab top 10 stories and print out the: Title, Discussion Link, and Comments
# Sort it based on Number of comments

submission_sublist = []

for sub_id in submission_ids[:10]: # slicing --> from element 0 to 10 
    # make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{sub_id}.json" # {sub_id} iterates thru each ID in submission IDs list
    r = requests.get(url)
    #print(f"id: {sub_id}\t\tstatus:{r.status_code}")

    # The response is a dictionary, so save it to a dictionary variable
    response_dict = r.json() # r.json converts json objects into python objects

    # Create a new dictionary of just the data you need
    a_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={sub_id}",
        'comments': response_dict['descendants']
    }

    # add this dictionary to your final list
    submission_sublist.append(a_dict)

print(submission_sublist)

# Method 1: submission_sublist = sorted(submission_sublist, key=lambda x:x['comments'], reverse=True)

# Method 2:
from operator import itemgetter
submission_sublist = sorted(submission_sublist, key=itemgetter('comments'), reverse=True) 

for d in submission_sublist:
    print(f"Title: {d['title']}")
    print(f"Discussion link: {d['hn_link']}")
    print(f"No. of comments: {d['comments']}\n")