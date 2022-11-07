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

# List Comprehension Syntax 7 Examples:
fruits = ["apple", "banana", "cherry", "orange"]
new_list2 = [x for x in fruits if "a" in x]
new_list3 = [x.upper() for x in fruits]

print(new_list2)
print(new_list3)

new_list4 = [x for x in range(10)]
new_list5 = [x for x in range(10) if x > 5]

print(new_list4)
print(new_list5)

# List Comprehension to manipulate the output
fruits = ["apple", "banana", "cherry", "orange"]
new_list6 = [x if x != "banana" else "orange" for x in fruits]

print(new_list6)

new_list7 = [True if x == "banana" else False for x in fruits]

print(new_list7)