# dictionary methods

NFL_Teams = {
    'New York': 'Giants',
    'Los Angeles': 'Rams',
    'Houston': 'Texans',
    'Dallas': 'Cowboys',
    'San Francisco': '49ers',
    'Chicago': 'Bears'
}

# NFL_Teams.clear()
# print(NFL_Teams)

# finding keys and values 
# print(list(NFL_Teams.keys()))
# print(list(NFL_Teams.values()))

# get method 
get_method = NFL_Teams.get('New York')
print(get_method)

# pop method 
pop_method = NFL_Teams.pop('Chicago')
print(pop_method)

# popitem method 
pop_item_method = NFL_Teams.popitem()
print(pop_item_method)

# update method 
dict1 = {'age1': 23, 'age2': 25, 'age3': 27, 'age4': 29}
dict2 = {'age5': 31, 'age6': 33, 'age7': 35}

dict1.update(dict2)
print(dict1)
