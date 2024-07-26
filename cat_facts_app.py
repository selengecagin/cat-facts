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

def save_facts_to_db(facts):
    for fact in facts:
        insert_fact(fact['text'])

def display_facts():
    facts = get_all_facts()
    print("\nCat Facts in the Database:")
    for fact in facts:
        print(f"ID: {fact[0]}, Fact: {fact[1]}, Created At: {fact[2]}")

def main():
    create_table()
    facts = fetch_cat_facts()
    if facts:
        save_facts_to_db(facts)
        print("Cat facts successfully saved to the database.")
        display_facts()
    else:
        print("Failed to fetch cat facts.")

if __name__ == "__main__":
    main()
