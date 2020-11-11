def overwrite(s):
    for number in range(0, 10):
        if str(number) in s:
            s = s.replace(str(number), number*"!")
    return s

print(overwrite("1Hello 2World4"))