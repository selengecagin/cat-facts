import requests
from database_operations import create_table, insert_fact, get_all_facts

def fetch_cat_facts():
    url = "https://cat-fact.herokuapp.com/facts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"API request failed. Status code: {response.status_code}")
        return None
