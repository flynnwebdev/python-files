# with open('shopping-list.txt', 'r') as f:
#   for line in f:
#     print(f'Item: {line.strip()}')
#   # data = f.readline().strip()
#   # print(data)

# shows = [
#   'The Mandalorian',
#   'The Witcher',
#   'The X Files',
#   'Star Trek: Picard'
# ]

# with open('tv-shows.txt', 'w') as f:
#   f.write('\n'.join(shows))
import csv

# with open('people.csv') as f:
#   reader = csv.DictReader(f) # Create a reader object based on the file object
#   for row in reader:
#     # print(row)
#     print(f"{row['name']} is {row['age']} years old and {row['height']}cm tall")

menu = [
  {'item': 'Cappuccino', 'hello': None, 'price': 5.50},
  {'item': 'English Breakfast Tea', 'price': 5},
  {'item': 'Blueberry Muffin', 'price': 6}
]

# with open('cafe-menu.csv', 'w') as f:
#   writer = csv.DictWriter(f, menu[0].keys())
#   writer.writeheader()
#   writer.writerows(menu)

import json

# with open('movies.json') as f:
#   movies = json.load(f)
#   print(movies[0]['director'])

with open('cafe-menu.json', 'w') as f:
  json.dump(menu, f, indent=4)
