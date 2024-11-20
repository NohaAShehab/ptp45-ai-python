

# display data in table

users= [
    {"id":1, "name": "Israa", "track": "ai", "salary":5000},
    {"id":2, "name": "Mariam", "track": "ai", "salary":50000},
    {"id": 3, "name": "Israa", "track": "ai", "salary":50000},
    {"id": 4, "name": "Adham", "track": "ai", "salary": -5000},
    {"id": 5, "name": "Sharkawy", "track": "ai", "salary": -5000},
]
print(users)


# print data in table
from tabulate import tabulate
# print(tabulate(users))

print(tabulate(users, headers="keys",  tablefmt="fancy_grid"))

import emoji
print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))