def count_vowels(sentence):
    v = 0
    sentence = sentence.lower()
    for i in range(0, len(sentence) - 1):
        vowels = ["a", "e", "i", "o", "u"]
        print(i)
        for b in range(0, len(vowels) - 1):
            if sentence[i] == vowels[b]:
                print(b)
                v += 1
               
print(count_vowels("Hello world"))