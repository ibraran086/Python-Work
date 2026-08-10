# #variables
# name="IBRAR"
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
# a=input("my name is.")
# b=input("my age is.")
# print(a)
# print(b)
# print(a+b)
# str="ibrar"
# age=(26,)
# # print(type(str))
# # print(len(str))
# # print(len(age))
# # print(type(age))
# print(str.capitalize())
# print(str.count("r"))
# print(str.endswith("r"))
# print(str.find("r"))
# print(str.index("a"))
# print(str.replace("i","I"))
# user=input("my name is.")
# print(len(user))
# var="i need many $.how much time for earn $."
# print(var.count("$"))
# print(var.replace("$",("dollars")))
# a=50
# b=40
# if(a==b):
#     print("equal")
# elif(a>b):
#     print("largest")
# else:
#     print("little")
# marks=71
# if(marks>=90):
#     print("grade A")
# elif(marks<90 and marks>80):
#     print("grade B")
# elif(marks<80 and marks>70):
#     print("grade C")
# else:
#     print("grade D")
# age=19
# if(age>=18):
#     if(age>80):
#         print("cannot drive")
#     else:
#         print("drive")
# a=47
# if(a%2==0):
#     print("even")
# else:
#     print("odd")
# a=43
# b=6
# c=123
# if(a>c and a>b):
#     print("greatest",a)
# elif(b>a and b>c):
#     print("greatest",b)
# else:
#     print("greatest",c)
# a=7
# if(a%7==0):
#     print("multi num")
# else:
#     print("not multi")
# list=[1,7,5,3,1,2,0,8]
# print(type(list))
# print(len(list))
# list[4]=9
# print(list)
# print(list[0:6])
# print(list[-5:-1])
# print(list[6])
# list=[5,6,3,2,9,5]
# list.append(5)
# print(list)
# list.copy()
# print(list)
#list=[9,1,8,2,7,3,3]
# print(list.count(3))
# list.remove(3)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.insert(5,0)
# print(list)
# list.pop(0)
# print(list)
# tup=(1,29,20,1)
#print(type(tup))
# print(len(tup))
# tup=(3,1,9,6,9)
# #print(tup.count(9))
# print(tup.index(9))
# a=input("1st movie name is:")
# b=input("2nd movie name is:")
# c=input("3rd movie name is:")
# print(a)
# print(b)
# print(c)
# list=[a,b,c]
# print(list)
# list=[1,2,3,2,5]
# list2=list.copy()#1,2,3,2,5
# list2.reverse()#5,2,3,2,1
# if(list==list2):
#     print("palinfrome")
# else:
#     print("not palindrome") 
# tup=["c","d","a","a","b","b","a"]
# # print(tup.count("a"))
# tup.sort()
# print(tup)
dic={
    "name":"ibrar",
    "other":{
        "age":26,
        "result":"PASS",
    }
}
# print(type(dic))
# print(len(dic))
# dic["nick name"]="Ibrari"
# print(dic)
# print(list(dic.keys()))
# print(list(dic.values()))
# print(list(dic.items()))
# print(dic.get("other"))
dic.update({"city":"sahiwal"})
print(dic)
print(dic.keys())
