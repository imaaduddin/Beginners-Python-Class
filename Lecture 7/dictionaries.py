# a dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair
# keys, can be integers, strings or tuples, but have to be unique, values can be of any type

"""
We can define a dictionary by enclosing a comma-separated list of key-value
pairs in curly braces ({}). A colon (:) separates each key from its associated
value
"""

# in the following example the key would be the cities and the value is the team names (Giants, Rams, etc,)

NFL_Teams = {
    'New York': 'Giants',
    'Los Angeles': 'Rams',
    'Houston': 'Texans',
    'Dallas': 'Cowboys',
    'San Francisco': '49ers',
    'Chicago': 'Bears'
}

print(NFL_Teams)

# Lists vs Dictionaries 
# with dictionaries objects are retrieved by key name, unordered and can’t be sorted
# with lists, objects are retrieved by location, ordered sequence can be indexed or sliced

# Another way to write a dictionary 
word_count = dict (hello = 4, hi = 1, that= 10, this = 70)
print(word_count)

# Create dictionary using a list of tuples 
NBA_team = dict([('New York', 'Knicks'), ('Boston', 'Celtics'),
('Houston', 'Rockets'), ('Los Angeles', 'Lakers'), ('Dallas', 'Mavericks')])
print(NBA_team)

# Creating a dictionary using two lists 
# List of strings
str_lst = ["Hello", "hi", "there", "at", "this"]
int_lst = [7, 10, 45, 23, 77]

# Merge the 2 lists to create a dictionary
word_count2 = dict( zip(str_lst, int_lst ))
print(word_count2)