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