def Counr_Of_alphabet(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
g = input("სიტყვა:")
result = Counr_Of_alphabet(g)
print(result)
