pizzas = ['margharita', 'fungi', 'capicioza']

friend_pizzas = pizzas[0:3]

pizzas.append('napoletana')
friend_pizzas.append('vegetariana')

print("\nMy favourite pizzas are:")
for pizza in pizzas:
	print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza.title())
