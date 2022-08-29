favorite_fruits=['apple', 'banana' , 'cherry']
fruits=str(input("Enter your favorite fruits: "))
if fruits in favorite_fruits:
    print("Your favorite fruits " + fruits  + " include in the list!")
else:
    print("It's not on the list")