class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Name of mthis reustarant: " + self.restaurant_name.title() + ".")
        print("Cuisine: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Restaurant opening hours from 09:00 to 23:00")

restaurant = Restaurant('Mamacita', 'franch')
restaurant.describe_restaurant()

restaurants = Restaurant('Berezka', 'belarus')
restaurants.describe_restaurant()
