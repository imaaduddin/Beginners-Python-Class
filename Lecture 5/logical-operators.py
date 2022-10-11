# and - everything needs to be True
# or - if one operand is True it's fine
# not - will result True if what you're checking is False

# not example: 
# turning True to False
# Turning False to true

age = 27
name = input('What is your name? ')

if age == 24 or name == 'Imaad':
    print('Correct Info!')
else:
    print('Incorrect Info!')

# length of name has to be at least 10 
# has to have special character 
# has to have a number 


if not name:
    print('Name is empty')
else:
    print('Printed name!')