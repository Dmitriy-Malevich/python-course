print("This is a calculator")
print("Enter 'q' to exit")

while True:
    number1 = input("\nFirst number: ")
    number2 = input("Second number: ")
    if number1 and number2 == 'q':
        break
    try:
        numbers= int(number1) + int(number2)
    except ValueError:
        print("Enter numbers")
    else:
        print(numbers)