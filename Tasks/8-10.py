
from unicodedata import name


def show_magicians(names):
    print("Names magicians: ")
    for name in names:
        print(name.title())

def make_great(names):
    for name in names:
        print("Names magicians Great: " + str(name.title()) + "!")


names = ['dima', 'roma', 'alexey', 'ivan']
show_magicians(names)
make_great(names[:])