my_food_list = ['milk', 'bread', 'chees', 'juice', 'chocolate', 'pasta']

lucy_food_list = my_food_list[:]

my_food_list.append('joghurt')
my_food_list.append('donut')
my_food_list.append('fish')

for food in my_food_list:
	print(food.title())

print("")
	
for food in lucy_food_list:
	print(food.title())
