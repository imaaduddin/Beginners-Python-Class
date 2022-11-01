# Question 1:

# data = {'a':1,'b':2,'c':3, 'd':10,'e':18}
# print(data['d'], data.get('e'), data.get('de'))

# Question 2:

price = {'milk': 2.99, 'coffee': 2.5, 'bread': 2.5}
new_price = {'milk': 3.99, 'coffee': 2.99, 'gas': 3.99}
price.update(new_price)
print(price)