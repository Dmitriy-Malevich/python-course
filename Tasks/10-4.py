guest = r'D:\test\TXT\guest_book.txt'

text = "\nPlease your name: "
text += "\nEnter 'quit' when you are finished. "

while True:
    name = input(text)
    if name == 'quit':
        break
    else:
        print("Hello " + name.title() + "!")
        with open(guest, 'a') as file_object:
            file_object.write("\n" + name.title())
