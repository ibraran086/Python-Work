list=["HADI",2,14.400]
print(list)
list[0]="AHAD"
print(list)
print(len(list))
list.append("HADI")
list.append("AREESHA NOOR")
print(list)
list.copy()
print(list)
print(list.count(14.400))
list.extend("G")
print(list)
print(list.index("HADI"))
list.insert(3,6)
print(list)
list.pop(6)
print(list)
list.remove(2)
print(list)
list.reverse()
print(list)
num=[4,1,6,2,5,9]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2,8)
print(num)
tup=(1,3,5,"hadi")
print(tup)
print(type(tup))
tup=(1,2)
print(type(tup))

tup1=(5,4,7,2,9)
print(tup1.count(4))
print(tup1.index(7))
# movie1=input("enter movie:")
# movie2=input("enter movie:")
# movie3=input("enter movie:")
# movie4=[movie1,movie2,movie3]

# print(movie4)
list=[1,2,3,2,1]
list2=list.copy()
list2.reverse()
if(list==list2):
    print("Palindrome")
else:
    print("Not Palindrome")


list=["C","D","A","A","B","B","A"]
list.sort()
print(list)
print(list.count("A"))
