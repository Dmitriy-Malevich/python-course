from fileinput import filename


filename = r'D:\test\Tasks\learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

    string = ''
    for line in lines:
        string += line

print(string*3)