class a :
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    @classmethod
    def printname(cls,name):
        cls.name = name
        print(cls.name)

    @staticmethod
    def printage(age):
        print(age)

obj = a("meshw", 21)
obj.printname("meshw")

a.printage(25)
print(obj.age)
a.printname("jack")
print(obj.name)
