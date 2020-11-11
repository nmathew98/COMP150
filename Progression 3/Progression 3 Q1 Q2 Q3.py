def booleanConverter(bool):
    print(bool)
    print(str(bool))
    print(int(bool))
    print(float(bool))

booleanConverter(True)

def isMultiple(x, y):
    return (y%x == 0)

print('is 9 a multiple of 3?', isMultiple(3, 9))
print('is 4 a multiple of 5?', isMultiple(5, 4))

def isSameType(x, y):
    return (type(x) == type(y))

print('is 9 the same type as "hello" ?', isSameType(9, 'hello'))