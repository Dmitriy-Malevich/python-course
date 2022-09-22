from fileinput import filename


def count_words(filename): 
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
       pass
    else:
        #Подсчет приблизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = r'D:\test\TXT\alice.txt'
count_words(filename)