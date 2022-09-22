guest = r'D:\test\TXT\10-5.txt'
enter ="Why do you like programming? "
enter += "\nPress to exit 'quit'"

while True:
    entered = input(enter)
    if entered == 'quit':
        break
    else:
        with open(guest, 'a') as file_object:
            file_object.write("\n" + entered.title())