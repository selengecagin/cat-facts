# Cat Facts Fetcher

This Python application fetches cat facts from an API and saves them into an SQLite database. It also provides functionality to display the saved cat facts.

## Features

- **API Request**: Fetches cat facts from the Cat Facts API.
- **Database Creation**: Creates an SQLite database to store the fetched cat facts.
- **Data Insertion**: Saves the cat facts into the SQLite database.
- **Data Display**: Displays the saved cat facts in the terminal/PowerShell.

## Requirements

- Python 3.x
- `requests` library: Install with `pip install requests`
- `sqlite3` library (comes with Python standard library)

## Installation

### Clone the Repository:
git clone https://github.com/yourusername/cat-facts-fetcher.git
cd cat-facts-fetcher

### Install Dependencies:
pip install requests

### Run the Application:
python main.py

## Functionality:
- The application will create an SQLite database named cat_facts.db if it doesn't already exist.
- It will fetch cat facts from the API and save them into the database.
- Finally, it will display the saved cat facts in the terminal/PowerShell.
