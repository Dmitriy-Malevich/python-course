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

class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privilegies = Privileges()
    

#admin = Admin('dmitriy', 'malevich', 23, 'minsk')
#admin.privilegies = ['Разрешено банить пользователей']
#admin.describe_user()
#admin.show_privileges()

class Privileges():
    def __init__(self, privilegies = []):
        self.privilegies = privilegies
    def show_privileges(self):
        for privilegie in self.privilegies:
            print("Admin :" + " " + privilegie)

admin = Admin('dmitriy', 'malevich', 23, 'minsk')
admin.privilegies.privilegies = ['Разрешено банить пользователей', 'Запрещено банить пользователей']
admin.privilegies.show_privileges()