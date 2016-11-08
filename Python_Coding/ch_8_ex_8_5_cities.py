def describe_city(city_name, country_name='united states'):
    """Display information about a city."""
    print("\n" + city_name.title() + " is in " + country_name.title())

describe_city(city_name='san diego')
describe_city(city_name='richmond')
describe_city(city_name='havana', country_name='cuba')
