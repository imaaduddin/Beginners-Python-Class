#Sets
fruit_set = {"apple", "banana", "cherry"}
print(fruit_set)

set1 = {"abc", 34, True, 40, "male"} # can take all elements type

# Sets methods
fruits = {"apple", "banana", "cherry", "pear", "watermelon"}
print("banana" in fruits) #to check an item is in a set

fruits.add("mango")
print(fruits)

# Sets concatenation
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(fruits)
my_fruits = ["kiwi", "orange", "apple"]
fruits.update(my_fruits)
print(type(fruits))

#Sets remove
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

print(fruits)