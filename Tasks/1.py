man1 = {'name': 'Ivan', 'city': 'Moscow'}
man2 = {'name': 'Richard', 'city': 'London'}
people = [man1, man2]
for man in people:
    print(f"Name: {man['name']} City: {man['city']}")