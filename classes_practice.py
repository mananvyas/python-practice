class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "merc"
car1.kind = "sports car"
car1.color = "blue"
#car1.value = 500


car2 = Vehicle()
car2.name = "fer"
car2.kind = "utility"
car2.color = "Red"
car2.value = 23000
print(car1.description())
print(car2.description())