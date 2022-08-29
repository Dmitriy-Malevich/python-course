from operator import ne


people=['anna', 'bob', 'egor']
#people.remove('anna')
#print(people)
#people.append('sanya')
print(people)
print("\n\t Invited for dinner: " + people[0])
print("\n\t Invited for dinner: " + people[1])
print("\n\t Invited for dinner: " + people[2])
#print("\n\t won't come to dinner: " + people[2])
new_people=people.pop(1)
print("\n\t won't come to dinner: " + new_people)
new_people=people.append('pimp')
print(people)