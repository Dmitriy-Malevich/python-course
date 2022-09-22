import json

filename = 'fnumbers.json'
with open(filename) as f_obj:
    number = json.load(f_obj)
    print("I know you favorite numbers, is " + number + "!")