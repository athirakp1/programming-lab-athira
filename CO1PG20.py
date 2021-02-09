list = [9, 16, 23, 32, 45]
print ("Original list:",list)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print ("list after removing EVEN numbers:",list)