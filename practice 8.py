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

class Bank:
    bank_name="United Bank"
    def __init__(self,employees,manager_name,accountant_name,sweeper):
        self.employees=employees
        self.manager_name=manager_name
        self.accountant_name=accountant_name
        self.sweeper=sweeper
bank=Bank(3,"UMAIR","IBRAR","ABDUL GANI")
print(Bank.bank_name,bank.employees,bank.manager_name,bank.accountant_name,bank.sweeper)

class Blueprint():
    company="BMW"
    def __init__(self,feature1,feature2,feature3):
        self.feature1=feature1
        self.feature2=feature2
        self.feature3=feature3
    def car(self):
        battery=100
        if(battery==100):
            print("battery full")
            print("you can drive your car.")
        else:
            print("waiting for full charging.")
car1=Blueprint("electric","fully automatic","remote control")
print(car1.company,car1.feature1,car1.feature2,car1.feature3)
car1.car()


class Student:
    collage_name="Govt collage"
    def __init__(self,name,phy,chem,math):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.math=math
    def average(self):
        average=(self.phy+self.chem+self.math)/3
        return average
s1=Student("hadi",99,98,97)
print(s1.collage_name,s1.name,s1.phy,s1.chem,s1.math)
print(s1.average())

class School:
    name="ummul_qura"
    def __init__(self,name,clas,roll_no,grade):
        self.name=name
        self.clas=clas
        self.roll_no=roll_no
        self.grade=grade
student1=School("hadi","play_group","1","A+")
print(School.name,student1.name,student1.clas,student1.roll_no,student1.grade)


class Student:
    name="GS School"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():
        print(s1.name)
    def average(self):
        sum=0
        for avg in self.marks:
            sum+=avg
        print("hi your average score is:",(sum)/3,"%")
s1=Student("Ahad",[99,98,97])
print(Student.name,s1.name,s1.marks)
s1.average()
s1.name="AREESHA NOOR"
s1.marks=[99,99,98]
print(s1.name)
s1.average()
s1.hello()

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.acc=True
        self.clutch=True
        print("car start...")
car1=Car()
car1.start()

class Account:
    @staticmethod
    def name():
        print("UBL")
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance-=amount
        print(amount)
    def credit(self,remain):
        self.balance+=remain
        print(remain)
    def get_balance(self):
        return self.balance
user=Account(50000,292238505)
user.debit(10000)
user.credit(20000)
print(user.get_balance())