def make_album(album, executor):
    albums = {'album': album, 'executor':executor}
    return albums

while True:
    print("\nEnter album and executor: ")
    print("(Enter 'q' at any time to quit)")
    a_albums = input("Enter album: ")
    if a_albums == 'q':
        break
    e_executor = input("Enter executor: ")
    if e_executor == 'q':
        break

makes_album = make_album(a_albums,e_executor)
print("\nHello, " + str(makes_album) + "!")