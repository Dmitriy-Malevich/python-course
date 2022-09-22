import json


filename = 'fnumbers.json'
try:
    with open(filename) as f_obj:
        number = json.load(f_obj)
        print("I know you favorite numbers, is " + number + "!")
except FileNotFoundError:
    numbers = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)

