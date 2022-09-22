import json

numbers = input("Enter your favorite number: ")
filename = 'fnumbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)