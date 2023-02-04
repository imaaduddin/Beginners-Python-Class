employee_file = open("employees.txt", "r")

for employee in employee_file.read_lines():
    print(employee)

employee_file.close()

# file write

employee_file = open("employees.txt", "w") # also try "a" for append
employee_file.write("\nKelly - Customer Service")
employee_file.close()