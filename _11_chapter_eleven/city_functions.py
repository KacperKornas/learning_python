def city_country(city, country, population=""):
    """Print a statement about the city and country."""
    if population == "":
        output_string = f"{city.title()} {country.title()}"
    else:
        output_string = f"{city.title()} {country.title()} - population {population}"
    return output_string
