def make_car(manufactured, brand, **other):
    profile = {}
    profile['manufactured'] = manufactured
    profile['brand'] = brand
    for key, value in other.items():
        profile[key] = value
        return profile
    
car = make_car('subaru', 'outback', color = 'blue', tow_package = 'True')
print(car)