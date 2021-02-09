a=input()

b=input()

x=a[1:2]

a=a.replace(a[1:2],b[1:2])

b=b.replace(b[1:2],x)

print(a,b)
