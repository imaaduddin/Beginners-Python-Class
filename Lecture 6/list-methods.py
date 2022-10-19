# Add something to a list append()
# The append() will add whatever you'd like to the end of a list

# fruits_list = ['orange', 'watermelon', 'grapes', 'mango']
# fruits_list.append('pineapple')
# print(fruits_list)

# Insert at a specific index we use the insert() method
# fruits_list = ['orange', 'watermelon', 'grapes', 'mango']
# fruits_list.insert(2, 'apple')
# print(fruits_list)

# To combine a list we can use + or the extend() method
# list1 = ['PlayStation', 'Xbox']
# list2 = ['Nintendo', 'PC']
# list1.extend(list2)
# print(list1)

# To remove an item from a list we remove() and put whatever item we would like removed inside the parenthesis 
# superheros = ['Spider-Man', 'Batman', 'Iron Man', 'Captain America', 'Super Man']
# superheros.remove('Captain America')
# print(superheros)


# To sort a list we use the sort() method
# numbers = [6, 2, 10, 3, 1, 13, 5, 18]
# numbers.sort()
# print(numbers)

# To sort in descending order we would do this
# numbers.sort(reverse=True)
# print(numbers)

# list copying we use the copy() method
list1 = ['pizza', 'burgers', 'pasta']
new_list = list1.copy()
print(new_list)