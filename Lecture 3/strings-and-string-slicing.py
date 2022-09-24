# string[start:end:step]

# Remember that the index always starts at 0 and not 1


my_string = "It is a great day today!"

print(my_string[4]) # Prints out the 4th index of thr string

print(my_string[0:7]) # Start from the beginning and go to the 7th index 

print(my_string[0:9:3]) # Start from the beginning an go to the 9th index while skipping every third character

print(my_string[:-5:-1]) # Start from the end of the string and stop at the 5th last index

print(my_string[::-1]) # Reverse a string 