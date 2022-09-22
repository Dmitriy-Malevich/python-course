
class User():

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.pull_name = first_name + " " + last_name
        self.age = age
        self.city = city
        

    def describe_user(self):
        print("\nUsers: " + self.pull_name.title() + " " + str(self.age) + " City: " + self.city.title())

    def greet_user(self):
        print("Hello " + self.pull_name.title())

registarated = User('dmitriy', 'malevich', 24, 'minsk')
registarated.describe_user()
registarated.greet_user()

friends_registrated = User('roman', 'samusev', 23 , 'minsk')
friends_registrated.describe_user()
friends_registrated.greet_user()