# #HELLO WORLD
# print("Hello world")
# #Variales
# name="ibrar"
# age=26
# weight=63.200
# data=True
# other=None
# print(name)
# print(age)
# print(weight)
# print(data)
# print(other)
# print(type(name))
# print(type(age))
# print(type(weight))
# print(type(data))
# print(type(other))
# #input in python 
# a=input("my name is:")
# b=input("my age is:")
# c=input("my weight is:")
#string
# str="my name is ibrar"
# print(len(str))
# print(str.endswith("r"))
# print(str.replace("i","a"))
# print(str.capitalize())
# print(str.count("is"))
# print(str.find("m"))
# WAP to input user's first name and print its length.
# name=input("my name is:")
# print(len(name))
#WAP to find the occurance of $ in a string.
# str="my name is a big $."
# print(str.find("$"))
# print(str.count("$"))
#conditional statement
#marks=60
# if(marks==90):
#     print("grade A")
# elif(marks<80 and marks>70):
#     print("grade B")
# else:
#     print("FAIL")
#NESTING
# age=18
# if(age>=18):
#     if(age>=80):
#         print("not drive")
#     else:
#          print("drive") 
# WAP to check if a number enter by the user is odd or even.
# num=19
# if(num%2==0):
#     print("even")
# else:
#     print("odd")
# WAP to find the greatest number of 3 numbers entered by the user.
# a=41
# b=5
# c=9
# if(a>b and a>c ):
#     print("Greatest number A")
# elif(b>a and b>c):
#     print("Greatest number B")
# else:
#     print("Greatest number C")
# #WAP to check if a number is a multiply of 7 or not.
# num=63
# if(num%7==0):
#     print("YES")
# else:
#     print("NOT")
#types of operators
#arithmetic operators
# a=4
# b=2
# print(a+b)
# print(a-b)
# print(a/b)
# print(a**b)
# print(a%b)
# # retional operators
# a=4
# b=2
# print(a<b)
# print(a>b)
# print(a<=b)
# print(a>=b)
# print(a==b)
# print(a!=b)
# # assignment operators
# num=4
# num/=2
# print(num)
#logical operators
# a=4
# b=2
# print(not(a<b))
# print(a<b and a!=b)
# print(a<b or a!=b)
#type conversion
# a="4"
# b=3
# a=int("4")
# print(a-b)
#input in python
# a=input("my name is:")
# b=input("my age is:")
# c=input("my weight is:")
# d=input("my data is:")
# e=input("my other documents is:")
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#string
# a="hello"
# b="world"
# print(a+b)
# c=a+b
# print(len(c))
# print(c[0])
# print(c[0:4])
# print(c[-5:-1])
#list and tuples
#list in python
# list=[1,2,4.6,"Ibrar"]
# print(len(list))
# print(list[0:2])
# print(list[0])
# print(list[-3:-1])
# list method
# list=[1,2,4,2,1,3,7,9]
# list.append(5)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# list=[1,8,2,7,4,0,1,2]
# list.insert(4,8)
# print(list)
# list.remove(1)
# print(list)
# list.pop(1)
# print(list )
#tuples
# tup=(2,3,4,876,5)
# print(type(tup))
# tup2=(1,)
# print(type(tup2))
# tup3=()
# print(type(tup3))
# print(len(tup))
# print(tup[2:4])
# print(tup[-2:-1])
#tuple method
# tup=(2,3,4,876,5)
# print(tup.index(4))
# print(tup.count(876))
#WAP to ask the User to enter names of their 3 favorite movies & store them in a list.
# list=[]
# a=input("enter 1st movie:")
# b=input("enter 2nd movie:")
# c=input("enter 3rd movie:")
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)
# WAP if a list contain a palindrome of elements.(Hint use copy method)
#[1,2,3,2,1]
# list=[1,2,3,2,5]
# b=list.copy()
# print(b.reverse())
# if(list==b):
#     print("palindrome")
# else:
#     print("not palindrome")
#tuples
#tup=(1,6,4,2,8,0,3,3,3)
# print(len(tup))
# print(tup.count(3))
#print(tup.index(1))
#list
list=[1,9,2,8,3,7]
# print(len(list))
# list.append(4)
# print(list)
# list.reverse()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.remove(9)
# print(list)
# list.pop(-1)
# print(list)
# list.insert(1,4)
# print(list)
#WAP to check if a list comtains a palindrome of elements.(HINT:use copy method)
# list=[1,"abc","abc",1]
# list2=list.copy()
# list2.reverse()
# if(list==list2):
#     print("palimdrome")
# else:
#     print("not palimdrome")
# #WAP to count the number of students with the "A" grade in the following tuple.
# grade=("c","d","a","a","b","b","a")
# print(type(grade))
# print(grade.count("a"))
#solve the above value in a list & sort them from "A" TO "D".
list=["c","d","a","a","b","b","a"]
list.sort()
print(list)