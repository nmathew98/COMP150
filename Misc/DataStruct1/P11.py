def names(file_name):
    file = open(file_name)
    contents = file.readline().split()
    keys = ''
    values = ''
    while contents:
        keys += contents[0] + ' '
        values += contents[1] + ' '
        contents = file.readline().split()
    keys = keys.split()
    values = values.split()
    return dict(zip(keys, values))

first = names("Names_2007.txt")
second = names("Names_2017.txt")

names_first = first.keys()
names_second = second.keys()
combined = ''
# Combined should contain:  Ella, John, Mitchell, Xavier, Riptoe, Charlotte, Anthony, Jason, Wenger, Isaac, Ollie, Matthew, Nick, Gent
for x in names_first:
    combined += x + ' ' if combined.find(x) == -1 else ''
for y in names_second:
    combined += y + ' ' if combined.find(y) == -1 else ''
combined = combined.split()
print("Total names in alphabetical order:", sorted(combined))