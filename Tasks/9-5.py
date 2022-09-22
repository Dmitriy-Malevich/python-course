class User():

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.pull_name = first_name + " " + last_name
        self.age = age
        self.city = city
        self.login_attempts = 0
        

    def describe_user(self):
        print("\nUsers: " + self.pull_name.title() + " " + str(self.age) + " City: " + self.city.title())

    def greet_user(self):
        print("Hello " + self.pull_name.title())

    def increment_login_attemps(self):
        self.login_attempts += 1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

registarated = User('dmitriy', 'malevich', 24, 'minsk')
registarated.describe_user()
registarated.greet_user()

friends_registrated = User('roman', 'samusev', 23 , 'minsk')
friends_registrated.describe_user()
friends_registrated.greet_user()
friends_registrated.increment_login_attemps()
friends_registrated.reset_login_attempts()
friends_registrated.increment_login_attemps()
