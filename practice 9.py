class Name:
    def __init__(self,name):
        self.name=name
name1=Name("nomi")
print(name1.name)
name2=Name("rehmat")
print(name2.name)



class Car:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

car1=Car("AUDI","SILVER")
print(car1.name)
print(car1.colour)
del car1.colour
print(car1.colour)