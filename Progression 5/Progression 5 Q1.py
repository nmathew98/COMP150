def letter_count(file_name):
    file = open(file_name)
    all_lines = file.readlines()
    all_lines = all_lines.lower(all_lines)
    count = 0
    for ch in all_lines:
        count = count + 1 if ch.islower() else count
    
    return count

print(letter_count("russia.txt"))
print(letter_count("antigua.txt"))