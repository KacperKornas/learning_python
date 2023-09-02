# Starts with two lists, one with order another with finished order.
sandwich_orders = ['fish sandwich', 'cottage chees sandwich', 'ham sandwich', 'egg sandwich']
finished_sandwiches = []

# Take every name of sandwiches and print message with it.
# Move each sandwiches to finished_list.
while sandwich_orders:
    for sandwich_order in sandwich_orders:
        current_sandwich = sandwich_orders.pop()

        print(f"I'll made your {current_sandwich}.")
        finished_sandwiches.append(current_sandwich)

# Print all finished Sandwiches.
print("\n---Finished Sandwiches---\n")
for finish_sandwich in finished_sandwiches:
    print(f"* {finish_sandwich}")