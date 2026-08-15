class Student:
    name="HADI"
    address="main road sahiwal."
    phone="03216901105"
collage=Student()
print(collage.name,collage.address,collage.phone)

class Car_blueprint:
    name="mercedes"
    engine=1.6
    average="1ltr==14km"
car=Car_blueprint()
print(car.name)
print(car.engine)
print(car.average)

class Bed_blueprint:
    list=["woods","nails","glue","matrious"]
bed=Bed_blueprint()
print(bed.list)


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    print("adding new student in database...")
s1=Student("hadi",99)
print(s1.name,s1.marks)

class Blueprint:
    def __init__(self,name,result):
        self.name=name
        self.result=result
fan=Blueprint("ahad","pass")
print(fan.name)
print(fan.result)

class Machine_blueprint:
    def __init__(self,wire,moter):
        self.wire=wire
        self.moter=moter
machine=Machine_blueprint("10m","1 each")
print(machine.wire)
print(machine.moter)

class Laptop:
    def __init__(self,charger,handfree):
        self.charger=charger
        self.handfree=handfree
laptop=Laptop("500watt","double bass")
print(laptop.charger)
print(laptop.handfree)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=Student("areesha","1")
print(s1.name)
print(s1.age)
s2=Student("hadi","4")
print(s2.name)
print(s2.age)

class Blueprint:
    st1="hadi"
    st2="ahad"
    st3="areesha"
collage=Blueprint()
print(collage.st1,collage.st2,collage.st3)

class Result:
    def __init__(self,total,pas,fail):
        self.total=total
        self.pas=pas
        self.fail=fail
result=Result(24,14,10)
print(result.total)
print(result.pas)
print(result.fail)
 
class Home:
    marlas=3
home=Home()
print(home.marlas)

class House:
    def __init__(self,rooms,washrooms,garage,TV_launge):
        self.room=rooms
        self.washroom=washrooms
        self.garage=garage
        self.TV_launge=TV_launge
home=House("4EA","2EA","1EA","1EA")
print("rooms:",home.room,",washrooms:",home.washroom,",garage:",home.garage,",TV_Launge:",home.TV_launge)

