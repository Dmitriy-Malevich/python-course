def get_city_functions(country, city, population = ''):
    if population:
        city = country + ", " + city + " -population " + population
    else:
        city = country + ", " + city
    return city.title() 