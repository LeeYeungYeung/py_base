def get_city_and_country(city, country, population=''):
    if population:
        full_name = f"{city}, {country}, population: {population}"
    else:
        full_name = f"{city}, {country}"
    return full_name.title()