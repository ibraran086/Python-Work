# class Student:
#     name="AHAD"
# s1=Student()
# print(s1.name)
# del s1
# print(s1)
# class Result:
#     school_name="Govt high school"
#     def __init__(self,class_stu,total_stu,pass_stu,fail_stu):
#         self.class_stu=class_stu
#         self.total_stu=total_stu
#         self.pass_stu=pass_stu
#         self.fail_stu=fail_stu
#     def avg(self):
#         total=100
#         p=50
#         f=50
#         avg=(p+f)/2
#         print(avg)
# st1=Result("10th",100,50,50)
# print(st1.school_name,st1.class_stu,st1.total_stu,st1.pass_stu,st1.fail_stu)
# st1.avg()
# del st1.class_stu
# class Account():
#     def __init__(self,acc_no,password):
#         self.acc_no=acc_no
#         self.__password=password
#     def reset_pass(self):
#         print(self.__password)
# per=Account(292238505,860000)
# print(per.acc_no)

# per.reset_pass()
# class Car():
#     @staticmethod
#     def start():
#         print("start car")
#     @staticmethod
#     def stop():
#         print("car stop")
# class Toyata_car(Car):
#     def __init__(self,brand):
#         self.brand=brand
# class Fortuner(Toyata_car):
#     def __init__(self,type):
#         self.type=type
# class Prius(Toyata_car):
#     def __init__(self,petrol):
#         self.petrol=petrol
# car1=Prius("10km per liter")
# print(car1.petrol)
# class Car:
#     @staticmethod
#     def start():
#         print("car start")
#     @staticmethod
#     def stop():
#         print("car stop")
# class Fortuner(Car):
#     @staticmethod
#     def type():
#         print("electric")
# car1=Fortuner()
# car1.start()
# class Result:
#     college="GCT"
#     def __init__(self,marks,grade):
#         self.marks=marks
#         self.grade=grade
# s1=Result(1045,"A")
# print(s1.marks)
# print(s1.grade)
# class Account:
#     def __init__(self,acc_no,password):
#         self.acc_no=acc_no
#         self.__password=password
#     def reset(self):
#         print(self.__password)
# user=Account(292238505,"asdf")
# print(user.acc_no)
# # print(user.__password)
# user.reset()
# class Child1:
#     var1="my name is Abdul Hadi."
# class Child2:
#     var2="my name is Abdul Ahad."
# class Child3(Child1,Child2):
#     var3="my name is Areesha Noor."
# fam=Child3()
# print(fam.var1)
# print(fam.var2)
# print(fam.var3)
# class Car:
#     def __init__(self,type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("car start")
#     def stop():
#         print("car stop")
# class Toyata(Car):
#     def __init__(self,name,type):
#         self.name=name
#         super().__init__(type)
#         super().start()
# car1=Toyata("prius","electric")
# print(car1.type)
# class Car:
#     def __init__(self,name):
#         self.name=name
#     @staticmethod
#     def start():
#             print("Car start")
#     @staticmethod
#     def stop():
#         print("Car stop")
# car1=Car("Hyondai")
# print(car1.name)
# car1.start()
# class Blueprint():
#      name="Abdul Hadi"
#      Class="Play group"
# son=Blueprint()
# print(son.name)
# print(son.Class)
# class Design:
#      Owner="IBRAR"
#      def __init__(self,rooms,washrooms,flour):
#           self.rooms=rooms
#           self.washrooms=washrooms
#           self.flour=flour
# house=Design(4,5,3)
# print(house.flour)
# print(house.rooms)
# print(house.washrooms)
# print(house.Owner)
# class Sons:
#     @staticmethod
#     def name():
#           print("Abdul Hadi")
#     @staticmethod
#     def name2():
#          print("Abdul Ahad")
# s1=Sons()
# s1.name()
# s1.name2()
# class Student:
#      def __init__(self,name,marks):
#           self.name=name
#           self.marks=marks
#      def avg(self):
#           sum=0
#           for val in self.marks:
#            sum+=val
#           print("hi",s1.name,"your avg score is:",sum/3)
# s1=Student("Hadi",[99,98,97])
# print(s1.name,s1.marks)
# s1.avg()
# class School:
#      # sch="ummul qura"
#      @staticmethod
#      def name():
#           print("HADI")
#      @staticmethod
#      def name2():
#           print("AHAD")
# s1=School()
# # print(s1.sch)
# s1.name()
# s1.name2()
# class Car:
#      cluch=False
#      race=False
#      brk=False
#      def start(self):
#           cluch=True
#           race=True
#           print("car start")
# car1=Car()
# car1.start()
# class Account:
#      def __init__(self,balance,acc_no):
#           self.balance=balance
#           self.acc_no=acc_no
#      def debit(self,amount):
#           self.balance-=amount
#           print("HI","HADI","YOUR REMAIN BALANCE IS:",self.balance)
#      def credit(self,amount):
#           self.balance+=amount
#           print("HI","HADI","YOUR REMAIN BALANCE IS:",self.balance)
#      def remain(self):
#           return print(self.balance)
# user=Account(50000,292238505)
# print(user.acc_no,user.balance)
# user.debit(5000)
# user.credit(10000)
# user.remain()
# class Person:
#      name="HADI"
#      def change_name(self,name):
#           self.name=name
# p1=Person()
# chang_name="Ahad"
# print(p1.name)
# print(Person.name)
# class Person:
#     name="HADI"
# #     def changename(self,name):
# #         self.__class__.name="Areesha"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# p1=Person()
# p1.changename("Ahad")
# print(p1.name)
# print(Person.name)
# class Person:
#     name="HADI"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# #     def changename(self,name):
# #         self.__class__.name="Ahad"
# p1=Person()
# p1.changename("Ahad")
# print(p1.name)
# print(Person.name)
# class Student:
#     def __init__(self,phy,che,math):
#         self.phy=phy
#         self.che=che
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy+self.che+self.math)/3)+"%" 
# s1=Student(98,99,97)
# print(s1.percentage)
# s1.phy=86
# print(s1.percentage)
# class Estimate:
#     rooms=150000
#     washrooms=1,00,000
#     kitchen=70,000
#     def rooms_estimate(self):
#         self.rooms*=4
#         print(self.rooms)
#     def washrooms_estimate(self):
#         self.washrooms*=5
#         print(self.washrooms)
#     def kitchen_estimate(self):
#         self.kitchen*=2
#         print(self.kitchen)
#     def sum_total(self):
#         total=int([self.rooms+self.washrooms+self.kitchen])
#         count=0
#         for val in total:
#             count+=val
#             print(count)
# house=Estimate()
# house.sum_total()
# class Person:
#     name="Hadi"
#     def changename(self,name):
#         self.name=name
# p1=Person()
# p1.changename("Ahad")
# print(p1.name)
# print(Person.name)
# class Person:
#     name="Messi"
#     def fun(self,name):
#         Person.name=name
# player=Person()
# player.fun("Ronaldo")
# print(player.name)
# print(Person.name)
# class Person:
#     name="nomi"
#     # def fun(self,name):
#     #     self.__class__.name="hadi"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
        
# p1=Person()
# p1.changename("usman")
# print(p1.name)
# print(Person.name)
# class Stu:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     # def calcpercentage(self):
#     #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# stu1=Stu(99,98,97)
# print(stu1.percentage)
# stu1.phy=86
# # print(stu1.phy)
# # stu1.calcpercentage()
# print(stu1.percentage)
# class Person():
#     name="Hadi"
#     def changename(self,name):
#         self.name=name
# p1=Person()
# p1.changename("ahad")
# print(p1.name)
# print(Person.name)
# class Player:
#     name="ronaldo"
#     def fun(self,name):
#         self.name=name
# p1=Player()
# p1.fun("messi")
# print(p1.name)
# print(Player.name)
# class Student:
#     name="faizan"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# p1=Student()
# p1.changename("zeeshan")
# print(p1.name)
# print(Student.name)
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# s1=Student(99,98,97)
# s1.phy=88
# print(s1.percentage)
#class method
# class Student:
#     name="Ahad"
#     def changename(self,name):
#         self.__class__.name="Gulfishan"
# s1=Student()
# s1.changename("Hadi")
# print(s1.name)
# print(Student.name)
# class Mother:
#     name="Guriya"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# m1=Mother()
# m1.changename("Gulfishan")
# print(m1.name)
# print(Mother.name)
# #property
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#     @property
#     def calpercentage(self):
#         return str((self.phy+self.chem+self.math)/3)+"%"
# s1=Student(99,98,97)
# s1.phy=88
# print(s1.phy)
# print(s1.calpercentage)
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownum(self):
#         print(self.real,"i+",self.img,"j")
# num1=Complex(1,3)
# num1.shownum()
# num2=Complex(4,6)
# num2.shownum()
#polymorphism
# print(2+2)
# print("hello"+"world")
# print([1,2,3]+[4,5,6])
# class Num:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def fun(self):
#         print(self.real,"i+",self.img,"j")
#     def add(self,num2):
#         realnum=self.real + num2.real
#         imgnum=self.img +num2.img
#         return Num(realnum,imgnum)
# num1=Num(1,3)
# num1.fun()
# num2=Num(4,6)
# num2.fun()
# num3=num1.add(num2)
# num3.fun()
#pollymorphism
# print(1+4)
# print("start"+"end")
# print([1,2,3]+[4,5,6])
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def fun(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        realnum=self.real+num2.real
        imgnum=self.img+num2.img
        return Complex(self.real,imgnum)
num=Complex(1,4)
num.fun()
num2=Complex(4,8)
num2.fun()
num3=num+num2
num3.fun()
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
c1=Circle(21)
print(c1.area())
print(c1.perimeter())
class Employee:
    def __init__(self,role,dep,salary):
        self.role=role
        self.dep=dep
        self.salary=salary
    def showdetails(self):
        print("role=",self.role)
        print("dep=",self.dep)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","75000")
emp1=Engineer("FAHEEM",24)
emp1.showdetails()
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,order2):
       return self.price>order2.price
order1=Order("juice",100)
order2=Order("tea",50)
print(order1>order2)