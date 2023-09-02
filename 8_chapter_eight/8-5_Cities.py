def describe_city(city, country='czech'):
    """Describe a city."""
    print(f"{city.title()} is in {country.title()}.")
describe_city('Praga')
describe_city('Brno')
describe_city('Mediolan', 'Italy')