prompt = "Enter you age: "
active = True
while active:
    age = int(input(prompt))
    if age < 3:
        print("The entrance is free")
        active = False
    elif 3<=age<12:
        print("Entry free 10$ ")
        active = False
    else:
        print("Entry free 15$ ")
        active = False 