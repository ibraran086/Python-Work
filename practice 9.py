class Name:
    def __init__(self,name):
        self.name=name
name1=Name("nomi")
print(name1.name)
name2=Name("rehmat")
print(name2.name)
del name2
print(name2.name)
