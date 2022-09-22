
filename = r'D:\test\Tasks\learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    strings = ''

    for line in lines:
        strings += line
        strings = strings.replace('Python', 'C')

print(strings)



