# Iterating over a dictionary traditional way
# my_dict = {'a':1, 'b':2, 'c':3, 'd':10, 'e':18}
# new_dict = dict()

# for key, value in my_dict.items():
#     new_dict[key] = value
#     print(new_dict)

# One line with dictionary comprehension
# new_dict = {k:v for k,v in my_dict.items()}

# print(new_dict)

# Dictionary Comprehension with conditions
# % is an operation to get the remainder
# new_dict = {k1: k1*2 for k1 in range(1, 12) if k1%2 == 0}

# print(new_dict)

# Dictionary Comprehension
# old_price = {'milk': 2.99, 'coffee': 2.5, 'bread': 2.5}
# increase_by = 1.20 # 20% increase in price
# new_price = {item: value * increase_by for (item, value) in old_price.items()}

# print(new_price)

# Dictionary Comprehension with conditions
old_price = {'gas': 3.02, 'coffee': 2.5, 'bread': 2.5}
increase_by = 1.20 # 20%
gas_increase = 1.30 # 30%
new_price = {item: value * gas_increase if item == 'gas' else value * increase_by for (item, value) in old_price.items()}

print(new_price)