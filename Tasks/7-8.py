sandwich_orders = ['tuna', 'salmon', 'perch', 'cheese', 'beef']
finished_sandwich = []

while sandwich_orders:
    sanwich = sandwich_orders.pop()
    print("I made your " + sanwich + " sandwich")
    finished_sandwich.append(sanwich)
print("\nAll sandwiches:")
for finish_s in finished_sandwich:
    print(finish_s)