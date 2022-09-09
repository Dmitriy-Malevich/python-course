def make_pizza(*toppings):
    # Вывод списка заказанных дополнений.
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + str(topping))

#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')