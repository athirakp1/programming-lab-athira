y={'a':2,'d':4,'f':3,'g':1,'b':7,'c':6,'e':5} 
l=list(y.items())
l.sort()
print('Ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)
dict=dict(l) 
print("Dictionary",y)