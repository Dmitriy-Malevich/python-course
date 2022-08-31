favorite_places = {
    'dmitriy' : ['river', 'forest', 'village'],
    'ivan' : ['city', 'cafe', 'house' ],
    'roman' : ['jobs', 'score', 'village'],
}

for name,place in favorite_places.items():
    print("\nName: " + name)
    for places in place:
        print(places)
    