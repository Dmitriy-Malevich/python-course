vacation = {}
polling_active = True
while polling_active:
    name = input("What your name? ")
    place = input("Place vacation: ")
    vacation[name] = place
    repeat = input("Would you like to let another person responsed? (Yes/no)")
    if repeat == "no":
        polling_active = False
for name, place in vacation.items():
        print(name + " will rest in: " + place)