# Starts with lists sandwiches.
sandwich_orders = [
    'fish sandwich', 'pastrami', 'pastrami',
    'ham sandwich','pastrami', 'egg sandwich']

print("In deli has run out of pastrami.")

# Defining loop that check and delate 'pastrami'.
while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')


print(sandwich_orders)
