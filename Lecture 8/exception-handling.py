answer = None
data = {"age": 10}
n = int(input("Enter Number: "))

try:
    answer = data["age"] / n
    print("Will print if no exception") # just to see if this line executes
except ZeroDivisionError as e:
    print(e)
except Exception as e: # any other exception
    print("Caught any exception: ", e)
finally: # always execute
    print("Answer is:", answer)