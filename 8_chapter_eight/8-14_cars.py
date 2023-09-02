# Create functions which store information.
def cars_catalog(manufacturer, model, **other):
    """Stores information aboout cars."""

# Create invariant positions in the function.
    car_information = {}
    car_information['manufacturer_name'] = manufacturer.title()
    car_information['model_name'] = model.title()

# Create function which should accept an arbitrary number arguments.
    for key, value in other.items():
        car_information[key] = value
    return car_information

chevroler_catalog = cars_catalog('chevroet', 'camaro',
                                 color='black',
                                 engine=6.0)

print(chevroler_catalog)