#String formating

name = "Dor"
age = 24

#print("%s is of age %d" % (name,age))

data = ("john", "doe", 53.44)

format_string = "Hello %s %s. Your current balance is $%.2f."
print(format_string % data)