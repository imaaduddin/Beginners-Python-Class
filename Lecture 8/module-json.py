import json

# Some JSON:
# json_example = '{"name": "Imaad", "age": 24, "city": "Houston"}'

# parse the JSON variable:
# parse_example = json.loads(json_example)
# print(parse_example["age"])


# convert Python to JSON:
my_dict = {
    'name': 'Imaad',
    'age': 24,
    'city': 'Houston'
}

# convert to JSON:
x = json.dumps(my_dict)

# the result is a JSON string:
print(x)