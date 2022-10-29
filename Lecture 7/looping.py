# looping through a dictionary 
student_age = {'Jack': 32, 'Ritika': 31, 'Jack' : 22, 'Mary' : 21, 'Jackson' :
25 , 'John' : 55}

for key in student_age:
    print(key, '::' , student_age[key])
    
# another way (more efficient)
# this is the efficient method

for key, value in student_age.items():
    print(key, '::' , value)