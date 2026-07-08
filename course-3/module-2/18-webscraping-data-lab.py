# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
### YOUR CODE HERE ###

import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())

# Step 3.2: Extract the Required Data
### YOUR CODE HERE ###
table = soup.find('table')
rows = table.find('tbody').find_all('tr')
game_data = []

for row in rows:
    cols = row.find_all('td')
    game_dict = {
        'GameID': cols[0].text.strip(),
        'Team 1': cols[1].text.strip(),
        'Team 2': cols[2].text.strip(),
        'Expected Runs (Team 1)': cols[3].text.strip(),
        'Expected Runs (Team 2)': cols[4].text.strip(),
        'Over/Under': cols[5].text.strip(),
        'Moneyline Favorite': cols[6].text.strip()
    }
    game_data.append(game_dict)

print(game_data)



# Step 4.1: Convert to a DataFrame
# Import pandas
### YOUR CODE HERE ###

import pandas as pd # type: ignore

# Convert the game data into a pandas DataFrame
### YOUR CODE HERE ###
df = pd.DataFrame(game_data)


# Inspect the DataFrame
### YOUR CODE HERE ###
df.head()
df.info()

# Save and print the shaped data
### YOUR CODE HERE ###
print(df)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###
df.to_csv('sports_statistics.csv', index=False)
print("Data saved to sports_statistics.csv")