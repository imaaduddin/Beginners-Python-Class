print(5 < 10) # This will be True

print(5 <= 5) # This will be True as well b/c is equal to 5

# ==, !=, is, is not

# ==
a = 'Helloo'
b = 'Hello'

print(a == b) # This will print out False b/c the two strings are not the same

# is
a = [1, 2, 3]
b = a
c = a[:] # a is still [1,2,3]

print(a == b) # True

print(a == c) # This is True as well b/c nothing has changed with the variable a

print(a is b) # This will be True b/c b and a are equal 

print(a is c) # This will return False b/c the memory of both a and c are not the same

# !=
print(5 != 10) # This will print True b/c 5 is not equal to 10
print(5 != 5) # This will print False n/c 5 is equal to 5