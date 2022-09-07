from tkinter.font import names


def show_magicians(names):
    print("Names magicians: ")
    for name in names:
        print(name.title())

names = ['dima', 'roma', 'alexey', 'ivan']
show_magicians(names)