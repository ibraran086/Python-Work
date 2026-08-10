dic={
    "name":"ibrar"
}
print(dic)
dic["name"]="Ibrar Ansari"
print(dic)
print(dic.values())
print(dic.keys())
dic={
    "name":"AHAD",
    "score":{
        "chem":95,
        "phy":99,
        "math":100

    }
}
print(dic.keys())
print(dic.values())
dic={
    "name":"HADI",
    "record":{
        "weight":14.400,
        "height":3.4
    }
}
dic["name"]="Abdul Hadi"
dic["record"]["weight"]=15
print(dic.keys())
print(dic.values())
dic={
    "name":"Munir",
    "family":{
        "wife1":"Rashidan Bibi",
        "sons":2,
        "detail":{
            "first_son":"Umair Munir",
            "second_son":"Ibrar Munir"
        }
    }
}
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("family"))
dic.update({"wife2":"khadija"})
print(dic)
dic={
    "house":73,
    "members":4,
    "start":{
        "name":"Munir Ahmed",
        "wife":"Rashidan Bibi",
        "sons":2,
        "name1":"Umair",
        "name2":"Ibrar"
    }

}
print(list(dic.keys()))
print(tuple(dic.values()))
dic["house"]="73/6.R"
print(dic["house"])
print(dic["start"]["name"])
stu={
    "result":{
        "stu1":"PASS",
        "stu2":"FAIL",
        "grade":{
            "stu1":"C",
            "stu2":"A"
        }
    }
}
print(len(stu))
print(stu["result"]["grade"]["stu1"])
print(stu.items())
print(stu.get("result"))
stu.update({"total":"98%"})
print(stu)
dic={
    "family":{
        "total":6,
        "bhai":"umair",
        "bhabhi":"gulfishan",
        "child":{
            "total_ch":3,
            "name1":"hadi",
            "name2":"ahad",
            "name3":"areesha",
            "final":{
                "main":"Ibrar"
            }
        }
    }
}
print(dic)
dic={
    "result":{
        "phy":"pass",
        "chem":"fail",
        "math":"pass",
        "grade":{
            "stu1":"A+"
        }
    }
}
print(dic.items())
print(dic.get("result")["phy"])
dic.update({"com":"pass"})
print(dic)
set1={1,2,3,4}
set2={1,2,2,2}
print(set2)
print(set1)
nul_set=set()
print(type(nul_set))
stu={98,64,99,99}
print(stu)
stu.add(1000)
print(stu)
stu.remove(99)
print(stu)
stu.pop()
print(stu)
print(set1.intersection(set2))
dic={
    "table":("a piece of furniture","list of fact and figure"),
    "cat":"a small animal"
}
print(dic["table"])
print(dic["cat"])
list=["python","java","C++","python","javascript","java","python","java","C++","C"]
list2=set(list)
print("need classes:",len(list2))
# marks={}
# x=int(input("enter phy:"))
# marks.update({"phy":x})

# x=int(input("enter chem:"))
# marks.update({"chem":x})

# x=int(input("enter com:"))
# marks.update({"com":x})
# print(marks)

# result={}
# a=input("enter marks:")
# result.update({"phy":a})
# print(result)
values={9,"9.0"}
print(values)
