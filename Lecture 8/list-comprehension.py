# List Comprehension 

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Regular method (longer way of writing)
fruits = ["apple", "banana", "cherry", "orange"]
new_list = []

for x in fruits:
    new_list.append(x)
print(new_list)

# shorter way of writing the same code above
new_list = [x for x in fruits]
print(new_list)