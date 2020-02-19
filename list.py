mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(33)


print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

#Trying to access invalid item
print(mylist[10])