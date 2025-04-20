import requests
import json
from collections import Counter  # For Part 2 of assignment

url = 'https://api.fbi.gov/wanted/v1/list'

# Make the API request
r = requests.get(url)
data = r.json()

# Write a .json file in this repo
outfile = open('fbi.json', 'w')
json.dump(data,outfile,indent=4)

# Part 1 - Iterate thru each individual in the list
for person in data.get('items', []):
    warning_message = person.get('warning_message', '')
    if warning_message and "SHOULD BE CONSIDERED ARMED AND DANGEROUS" in warning_message.upper():
        name = person.get('title', 'N/A')
        fbi_link = person.get('url', 'N/A')
        gender = person.get('sex', 'N/A')
        subject = ', '.join(person.get('subjects', [])) if person.get('subjects') else 'N/A'

        print()
        print(f"Name: {name}")
        print(f"FBI Direct Link: {fbi_link}")
        print(f"Gender: {gender}")
        print(f"Subject: {subject}\n")

# Part 2 - List the different crimes (subjects) and how many 
# felons are convicted of those crimes in descending order of count

# Create a list to hold all subjects
all_subjects = []

# Extract subjects from each person
for person in data.get('items', []):
    subjects = person.get('subjects', []) # 'subjects' is key for accessing the crime types on API endpoint
    all_subjects.extend(subjects) # '.extend' adds all elements from 'subjects' list to the 'all_subejcts' list

# Count each subject
subject_counts = Counter(all_subjects) # 'Counter' class takes a list/iterable and counts how many times each item appears in it.

# Sort and display results
for subject, count in subject_counts.most_common():
    print(f"Crime: {subject} Count: {count}")
