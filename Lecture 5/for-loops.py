# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# iterate over a string
for x in "banana":
      print(x)

# another way to iterate over a string and see the index
index = 0
my_str = "I live in Houston. The weather is great today!"

for c in my_str:
    print(f"{index:2d}: {c}")
    index += 1

# iterating through a list (array)
fruits = ["apple", "banana", "cherry", "orange", "pear", "watermelon", "strawberry"]
for x in fruits:
  print(x)