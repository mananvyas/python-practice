#dictionaries
myphonebook = {}
myphonebook["person1"] = 121212
myphonebook["person2"] = 343434
myphonebook["person3"] = 55121212
myphonebook["person4"] = 44343434

print(myphonebook)

#Iterating using for loop

for name, number in myphonebook.items():
    print("Contact number of %s is %d" % (name, number))

#removing entry
del myphonebook["person1"]

print(myphonebook)