def iseveryasounikaluri(string):
    for i in string:
        result = string.count(i)
        if result > 1:
            return False 
        else: 
            return True
g = input("სიტყვა:")
obj = iseveryasounikaluri(g)
print(obj)