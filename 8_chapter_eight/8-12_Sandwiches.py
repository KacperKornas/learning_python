# Make function which print ordered sandwiches.
def sandwiches_order(*sandwiches):
    """Print ordered sandwiches."""
    print(f"\nOrdered sandwiches is: ")
    for sandwich in sandwiches:
        print(f"- {sandwich}")

sandwiches_order('pepperoni')
sandwiches_order('chees sandwich', 'egg sandwich')
sandwiches_order('egg sandwich', 'fish sandwich', 'chees sandwich')

