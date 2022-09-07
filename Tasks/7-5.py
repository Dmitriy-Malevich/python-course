prompt = "Enter you age: "
while True:
    age = int(input(prompt))
    if age < 3:
        print("The entrance is free")
    elif 3<=age<12:
        print("Entry free 10$ ")
    else:
        print("Entry free 15$ ") 
    break