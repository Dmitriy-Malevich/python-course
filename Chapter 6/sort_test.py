from cgitb import reset


cars=['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
#print("\nHere is the sorted list:")
#print(sorted(cars))
#print("Here is the original list:")
#cars.sort(reverse=True)
#print(cars)
cars.reverse()
print(cars)
print(len(cars))