#HTML
from bs4 import BeautifulSoup
from requests import get

response = get('https://epam.com')
soup = BeautifulSoup(response.text, 'html.parser')
sum_of_divs = 0

for tag in soup.find_all('div'):
   sum_of_divs += 1

print(sum_of_divs)

#SQL

import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE employees
             (number integer, name text)''')
c.execute("INSERT INTO employees VALUES ('1','Ivan')")
c.execute("INSERT INTO employees VALUES ('2','Alex')")
c.execute("INSERT INTO employees VALUES ('3','Anna')")

conn.commit()

for row in c.execute('SELECT * FROM employees'):
        print(row)

conn.close()