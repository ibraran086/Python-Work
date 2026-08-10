print('hello world')
#variables
name="Ibrar"
age=26
weight=64.100
data=True
other=None
print(name)
print(age)
print(weight)
print(data)
print(other)
print(type(name))
print(type(age))
print(type(weight))
print(type(data))
print(type(other))
#types of operators
#arithmetic operators
a=4
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
#Retional operators
a=4
a=4
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)
#assignment operators
num=4
num+=2
print(num)
#logical operators
a=4
b=3
print(not(a<b))
print(a>b and a<b)
print(a==b or a>b)
#Input in python
#l
c="4"
d="8"
c=int("4")
d=int("8")
print(c+d)
#string
str="my name is IBRAR"
str2="my age is 26"
print(str+str2)
str3="my name is umair"
print(len(str3))
print(str3[0:2])
print(str3[-4:-1])
#string functions
str="my name is Ibrar"
str=str.capitalize()
print(str)
print(str.endswith("r"))
print(str.replace("i","a"))
print(str.count("a"))
print(str.find("a"))
#write a program to input user name and print its length.
a=input("my name is:")
print(len(a))
#WAP to find the occurrence of '$'in a string.
a="i am a $"
print(a.find('$'))
print(a.replace("$","paisa")) 
#type conversion
#automatic 
a=4
b=2
print(a+b)
#manual casting
a="4"
b=8
a=int("4")
print(a+b)
#conditional statement
#grade student based on marks
marks=69
if(marks>=90):
    print("grade A")
    if(marks<90 and marks>=80):
        print("grade B")
elif(marks<80 and marks>=70):
    print("grade C")
else:
    print("grade D")        
#WAP to check if a number entered by the user is odd and even.
num=109
if(num%2==0): 
    print("even")
else:
    print("odd")
#WAP to find the greatest of 3 number enter by the user.
a=8
b=3
c=4
if(a>b and a>c):
    print("greatest number A")
elif(b>a and b>c):
    print("greatest number B")
else:
    print("greatest number C")
#WAP to check if a number is a multiply of 7 or not.
num=46
if(num%7==0):
    print("YES")
else:
    print("NOT")