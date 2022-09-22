def dogs(nicknames):
    try:
        with open(nicknames) as f_obj:
            names = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        pets = names.split()
        print(pets)

filename = r'D:\test\TXT\cats.txt'
dogs(filename)

filenames = r'D:\test\TXT\dogs.txt'
dogs(filenames)
