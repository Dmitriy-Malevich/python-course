numbers=list(range(1,10))
for number in numbers:
    if 0<number <= 1:
        print(str(number) + "st")
    elif 1<number <= 2:
        print(str(number) + "nd")
    elif 2<number <= 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
