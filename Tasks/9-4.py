class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nName of mthis reustarant: " + self.restaurant_name.title() + ".")
        print("Cuisine: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Restaurant opening hours from 09:00 to 23:00")

    def set_number_served(self):
        #self.number_served = amounts
        print("Serveted: " + str(self.number_served))

    def increment_number_served(self, increments):
        self.number_served += increments


restaurant = Restaurant('Mamacita', 'franch')
restaurant.describe_restaurant()
#restaurant.number_serveteds()

restaurants = Restaurant('Berezka', 'belarus')
restaurants.describe_restaurant()
restaurants.set_number_served()

restaurants = Restaurant('Berezka222', 'be111larus')
restaurants.increment_number_served(100)
restaurants.set_number_served()