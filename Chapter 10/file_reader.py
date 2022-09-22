file_path = 'D:/test/TXT/pi_digits.txt'
#file_path = r'D:\test\Chapter 10\pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    
    print(pi_string)
    print(len(pi_string))
    
    #contents = file_object.read()
    #print(contents.rstrip())