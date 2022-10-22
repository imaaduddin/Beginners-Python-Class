# Tuples 
# Tuples are ordered, unchangeable, and allow duplicate values

tuple1 = ('Imaad', 40, True, 'male')
tuple2 = ('Texas', 'Houston')

print(len(tuple1)) # to get the length

print(type(tuple2))

print(tuple1[1]) #to get the first element, same indexing as lists
print(tuple1 + tuple2) # to concatenate tuples

# Tuple Assignments 
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
(name, surname, bYear, movie, mYear, profession, birthplace) = julia

print(julia)