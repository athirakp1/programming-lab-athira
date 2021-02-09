def merge(dict1,dict2):
    return(dict1.update(dict2))
dict1 = {'a':2,'b':5,'c':13}
dict2 = {'d':6, 'e':10, 'f':12}
print(merge(dict1,dict2))
print(dict1)