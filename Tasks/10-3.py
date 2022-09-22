guest = r'D:\test\TXT\guest.txt'

with open(guest, 'w') as file_object:
    name = input("Enter your name: ")
    file_object.write(name)