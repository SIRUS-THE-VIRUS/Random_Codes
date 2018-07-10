# modify for the table that is on the website that you want to scrape
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
url = "https://www.w3schools.com/html/html_tables.asp"
# get the web url that has the table
try:
    # Get the source code of the page
    page = urllib.request.urlopen(url)
except Exception as e:
    print(e)
    pass
# use BeautifulSoup to analyze the source code from the page and store it in the soup
soup = BeautifulSoup(page, "html.parser")
# now we are looking for all the table and selecting the first one out of the list of tables on the website
table = soup.find_all('table')[0]
# pandas is used to create a new table dataframe for us.
new_table = pd.DataFrame(columns=['Company', 'Contact', 'Country'], index=range(1, 7))
row_number = -1
# For loop for storing the data collected into the new_table
for row in table.find_all('tr'):
    column_number = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_number, column_number] = column.get_text()
        column_number += 1
    row_number += 1
print(new_table)