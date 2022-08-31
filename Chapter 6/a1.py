my_foods=['pizza', 'falafel','pasta','chocolate','coctaile']
friends_foods=my_foods[:]
my_foods.append('lime')
friends_foods.append('apple')
for i in my_foods:
    print("My favorite foods: "+ i)
for n in friends_foods:
    print("\nMy friend's favorite food's:" + n)
