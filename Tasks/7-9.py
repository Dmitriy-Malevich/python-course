sandwich_orders = ['pastrami', 'tuna', 'salmon', 'pastrami', 'perch', 'cheese', 'beef', 'pastrami']
finished_sandwich = []

while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        sanwich = sandwich_orders.pop()
        print("I made your " + sanwich + " sandwich")
        finished_sandwich.append(sanwich)
print("\nAll sandwiches:")
for finish_s in finished_sandwich:
    print(finish_s)