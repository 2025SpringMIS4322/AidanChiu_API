import requests
import json


#random chuch norris jokes
random_url = "https://api.chucknorris.io/jokes/random"


#list of categories
category_url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
random_category_url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
search_url = "https://api.chucknorris.io/jokes/search?query={query}"




'''
Part I
The program should welcome the user by displaying a random chuck norris joke
'''
# Use random_url
r1 = requests.get(random_url)
random_joke = r1.json() # Auto creates a dictionary 
print(f"Welcome user: {random_joke['value']}\n")

'''
Part II
list the categories to the user and ask to pick a category
'''
# Use category_url

r2 = requests.get(category_url)
list_of_categories = r2.json()
print(f"List of categories: {list_of_categories}")
category_choice = input(f"Select a category from the list: ")
print()

    
        
'''
Part III
Display a joke based on the category picked by the user
'''

while True: 
    if category_choice not in list_of_categories:
        print('Please make a selection from the list')
    elif category_choice == '':
        print('Please enter something')
    else:
        url_category_choice = f"https://api.chucknorris.io/jokes/random?category={category_choice}"
        r_new_cat = requests.get(url_category_choice)
        r_new_cat_convert = r_new_cat.json()
        print(f"Here is the joke for '{category_choice}': {r_new_cat_convert['value']}\n")
        break

'''
Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''

query = input("Enter a few keywords from your favorite Chuck Norris joke: ")
search_url = f"https://api.chucknorris.io/jokes/search"

print()

r3 = requests.get(search_url, params = {"query": query})
new_query = r3.json()
results = new_query.get('result', [])

if results:
    print(f"\n Found {len(results)} matching joke(s):\n")
    for i, joke in enumerate(results, start = 1):
        print(f"{i}: {joke['value']}\n")
else:
    print('No jokes found with those keywords')


