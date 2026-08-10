# def fun(a,b):
#     return a+b
# sum=fun(4,2)
# print(sum)



def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
cal_sum(4,3)

def fun():
    print("hello")
fun()


def sum_calc(a,b):
    return(a+b)
print(sum_calc(4,4))
print(sum_calc(10,10))

def str_ing(a,b):
    return a+b
print(str_ing("hello","world"))
print(str_ing([1,2,3],[4,5,6]))
print(sum_calc((1,2,3),(4,5,6)))


def avg_fun(a,b,c):
    return (a+b+c)/3
print(avg_fun(1,2,3))


print("hello\nworld")


def pro(ulala):
    total=1000
    total-=ulala
    print(total)
    return total
pro(50)
pro(950)
pro(50)

print("hello\n""world")

print("hadi",end=" ")
print("ahad")

def fun(list):
    for i in list:
        print(i,end=" ")
    
fun(["name",26,63.900])


def fac_calc(n):
    fac=1
    for t in range(1,n+1):
        fac*=t
    print(fac)

fac_calc(5)



def convert(usd):
    pkr=usd*300
    print(usd,"usd=",pkr,"pkr")
convert(20)



# def fun(num):
#     if(num%2==0):
#         print("odd")
#     else:
#         print("even")
# fun(int(input("enter num:")))
# fun(int(input("enter num:")))


def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)


def fac(n):
    if(n==0 or n==1):
        return 1
    return fac(n-1)*n
print(fac(5))


def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))

def fun(n):
    if(n==0):
        return
    print(n)
    fun(n-1)
fun(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

print(fac(5))

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))

def fun(list,index):
    while index<len(list):
        print(list[index])
        index+=1
fun([1,5,2,5],0)



def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(5)

def fac(n):
    if(n==0 or n==1):
        return 1
    return fac(n-1)*n
print(fac(5))


def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))

def fun(list,ind=0):
    if(ind==len(list)):
        return
    print(list[ind])
    fun(list,ind+1)


fruits=["apple","banana","date"]
fun(fruits)



def ele(list,ind=0):
    if(ind==len(list)):
        return
    print(list[ind])
    ele(list,ind+1)
name=["umair","ibrar","munir"]
ele(name)

def fun(n):
    if(n==0):
        return 0
    print(n)
    fun(n-1)
fun(5)

def fac(n):
    if(n==0 or n==1):
        return 1
    return fac(n-1)*n
print(fac(5))

def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n
print(sum(5))


def fun(list,ind=0):
    if(ind==len(list)):
        return 
    print(list[ind])
    fun(list,ind+1)
name=["umair","ibrar","uzair"]
fun(name)

