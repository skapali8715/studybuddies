def stringy(size):
    counter = 1
    string = ''
    while counter < len(size) + 1: #While counter less than length of string entered
        if counter % 2 == 0: #if counter is even
            string += '0' #string becomes string concatenated with 0
        else:
            string += '1' #string becomes string concatenated with 1
        counter += 1
    
    print(string)
stringy('forthelulz')

#Mark