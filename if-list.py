
avilable_toppings=['mushrooms', 'alivies', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings=[]
a=input("Enter toppings: ")
requested_toppings.append(a)
#print(requested_toppings) #To view added toppings in list
for requested_topping in requested_toppings:
    if requested_topping in avilable_toppings:
        print("Adding " + requested_topping)
    else:
        print("Sorry we don't have " + str(requested_topping))