def get_word_longer_than(x):
    valid = False
    while not valid:
        userin = input("Please enter a word longer than " + str(x) + ": ")
        valid = (len(userin) > x) and (userin.find(' ') == -1) and (userin.isalpha() == True)
        print("Try again") if not valid else print(userin)
    
def first_x_vowels(file_name, x):
    """
    >>> first_x_vowels('test.txt', 10)
    'aouieieiie'
    >>> first_x_vowels('russia.txt', 50)
    'ioouiaoiieiaeeeeoeiaeioouiaeiiaoeEaeaaeioUieoeeaeo'
    >>> first_x_vowels('antigua.txt', 15)
    'iooAiuaaauaoiie'
    """
    file = open(file_name)
    contents = file.readline()
    result = ""
    while contents:
        for ch in contents:
            result += ch if ((ch in "aeiouAEIOU") and (len(result) < x)) else ""
        contents = file.readline()
    file.close()
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()