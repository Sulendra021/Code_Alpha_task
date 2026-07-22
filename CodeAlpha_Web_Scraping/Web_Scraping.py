import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

# Send a GET request with headers to avoid blocking
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# DEBUG: Check what tables exist
tables = soup.find_all('table')
print(f"Found {len(tables)} tables on the page")

# Option 1: Find by heading text (most reliable for Wikipedia)
heading = soup.find('span', {'id': '2025_Forbes_list'})
if heading:
    table = heading.find_parent().find_next('table')
else:
    # Option 2: Find the first table with 'wikitable' class
    table = soup.find('table', class_='wikitable')
    if not table:
        # Option 3: Find by class containing 'wikitable'
        table = soup.find('table', {'class': lambda c: c and 'wikitable' in c})

if table:
    print("Table found successfully!")
    
    # Extract all rows from the table
    rows = table.find_all('tr')
    
    # Extract headers from the first row
    header_row = rows[0]
    headers = [header.get_text(strip=True) for header in header_row.find_all('th')]
    
    # Extract data from all subsequent rows
    data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) == len(headers):
            row_data = [cell.get_text(strip=True) for cell in cells]
            data.append(row_data)
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data, columns=headers)
    print("First 10 rows of the Forbes 2025 list:")
    print(df.head(10))
    
    # Save to CSV
    df.to_csv('forbes_2025_india.csv', index=False)
    print(f"\n✓ Data saved to 'forbes_2025_india.csv' with {len(df)} rows")
    
else:
    print("Table not found!")
    # Debug: Print all table classes found
    for i, tbl in enumerate(tables):
        print(f"Table {i}: class = {tbl.get('class', 'No class')}")