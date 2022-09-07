prompt = "\n Enter toppings for pizza: "
while True:
    toppings = input(prompt)
    if toppings == "quit":
        break
    else:
        print("Toppings: " + toppings.title() + " added in pizza!")
