# f=open ("family","r")
# data=f.read()
# print(data)
# print(type(data))


# f=open("family","w")
# data=f.write("are you kiding me.\n""are you ok\n""any problem")
# print(data)
# f.close()

# f=open("family","r")
# data=f.read()
# print(data)
# f.close()

# f=open("family","w")
# data=f.write("my name is Ibrar.\nI am 26 years old.\nI am a software engineer.")
# print(data)
# f.close()

# f=open("family","r")
# data=f.read()
# print(data)
# f.close()

# f=open("family","r+")
# data=f.write("hello python.\ncan you listen me.")
# data2=f.read(data)
# print(data2)
# f.close()

# f=open("family","r")
# data=f.read(5)
# print(data)
# f.close()

# f=open("family","r")
# data=f.read()
# print(data)
# line1=f.readline()
# print(line1)
# line2=f.readline()
# print(line2)
# line3=f.readline()
# print(line3)
# f.close()

# f=open("family","a+")
# print(f.read())
# f.write("\nwhat is my data is correct.")
# f.write("\nif the data is wrong type wrong.")


# with open("family","r")as f:
#     print(f.read()) 

# import os
# os.remove("family")

# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing java.\nI like programming in java.")

# with open("practice.txt","r") as f:
#     data=f.read()
#     data2=data.replace("java","python")
#     print(data2)
# with open("practice.txt","w") as f:
#     f.write(data2)
# word="learning"
# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("Found")
#     else:
#         print("not Found")

# def check():
#     word="python"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1
#     return -1
# check()

# with open("practice.txt","r") as f:
#     print(f.read())
# with open("file","r") as f:
#     print(f.read())
# f.close()

# f=open("file","w")
# f.write("my name is ibrar.\ni am 26 years old.")


# import os
# os.remove("file")
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning file I/O\nusing java.\ni like programming in java.")
with open("practice.txt","r") as f:
    data=f.read()
    data2=data.replace("java","python")
    print(data2)
with open("practice.txt","w") as f:
    f.write(data2)
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(word in data):
        print("finding")
    else:
        print("not finding")
def check():
    word="learninga"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
print(check())

with open("data","r") as f:
    data=f.read()
    print(data)
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(int(num))
            num=""
        else:
            num+=data[i]
count=0
with open("data","r") as f:
    data2=f.read()
    print(data2)
    num=data2.split(",")
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)
count=0
with open("data","r") as f:
    data=f.read()
    print(data)
    num=data.split(",")
    print(num)
    for val in num:
        if(int(val)%2==0):
            count+=1
print(count)