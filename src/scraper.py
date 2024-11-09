import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.workerscompensationshop.com/workers-compensation-class-codes-alphabetical"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

table_root = soup.find('table', attrs={'class': 'table table-bordered shadow-sm mb-0'})
table = table_root.find('tbody')

# Now write the CSV with standard quoting
with open('jobcodes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, 
                       quoting=csv.QUOTE_MINIMAL,     # Quote only when necessary
                       doublequote=True)              # Double quotes to escape them
    
    writer.writerow(['code', 'description'])  # Header
    
    for row in table.findAll('tr'):
        cols = row.findAll('td')
        code = cols[0].text.strip()
        desc = cols[1].text.strip()
        writer.writerow([code, desc])