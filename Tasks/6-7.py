
friends_1= {
    'first_name' : 'dmitriy',
    'last_name' : 'malevich',
    'age' : 23,
    'city' : 'minsk',
}

friends_2= {
    'first_name' : 'roman',
    'last_name' : 'samusev',
    'age' : 24,
    'city' : 'minsk',
}

friends_3= {
    'first_name' : 'vlavislav',
    'last_name' : 'lapitskiy',
    'age' : 25,
    'city' : 'minsk',
}

people = [friends_1, friends_2, friends_3]

for peoples in people:
    full_name = peoples['first_name'] + " " + peoples['last_name']
    print("\nLast name: " + full_name.title() + " , " + str(peoples['age']) + " age, " + "location: " + peoples['city'] + ".") 
    #for peopless in peoples.items():
    #print(f"Name: {peoples['first_name']}  {peoples['last_name']}  {peoples[str('age')]}  {peoples['city']}")
   
  