def reverse(word):
    str = ""
    for i in word:
        str = i  + str
    return str
g = input("სიტყვა:")
result = reverse(g)
print(result) 