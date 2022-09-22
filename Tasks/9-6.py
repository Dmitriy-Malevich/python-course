class Restaurant():
    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Name of mthis reustarant: " + self.restaurant_name.title() + ".")
        print("Cuisine: " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("Restaurant opening hours from 09:00 to 23:00")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        for flavor in self.flavors:
            print("This is a " + flavor + " flavored ice cream.")

iceCreamStand = IceCreamStand('Kfc', 'ice cream')
iceCreamStand.flavors = ['ice cream', 'strawberry']

iceCreamStand.describe_restaurant()
iceCreamStand.show_flavors()
    