#Inheritance
class person:
    def __init__(self, name):
        self.name = name 

    def get_name(self):
        print(f"Name is {self.name}")

    def isemployee(self):
        return False
    
class employee(person):
    def isemployee(self):
        return True

obj = person("Jack")
obj.get_name()
print(obj.isemployee())

obj = employee("max")
obj.get_name()
print(obj.isemployee())


#super function
class student():
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, self.age)

class notstudent(student):
    def __init__(self, name, age) -> None:
        self.sname = name
        self.sage = age
        super().__init__(name, age)
        
    def displayinfo(self):
        super().display()

obj1 = notstudent("meshw",21)
obj1.displayinfo()

#Multiple Inheritance

class a:
    def __init__(self):
        self.str1 = "Hello"
        print(self.str1)

class b:
    def __init__(self) -> None:
        self.str2 = "world"
        print(self.str2)

class c(a, b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        print("derived")
    
    def printstr(self):
        print(self.str1,self.str2)
    
ob = c()
ob.printstr()

#multiple Inheritance 

class x:
    def __init__(self,name):
        self.name = name 
    
    def getname(self):
        return self.name

class y(x):
    def __init__(self,name,age):
        x.__init__(self,name)
        self.age = age

    def getage(self):
        return self.age

class z(y):
    def __init__(self,name,age,number):
        y.__init__(self,name,age)
        self.number = number

    def getnumber(self):
        return self.number
    
obj = z("jack",21,456456)
print(obj.getage(),obj.getname(),obj.getnumber())


# Hierarchical inheritance

class q:
    def __init__(self):
        self.name = "meshw"
        print(self.name)
    
class r(q):
    def __init__(self):
        self.age = 22
        q.__init__(self)
        print(self.age)

class s(q):
    def __init__(self):
        self.number = 33039
        q.__init__(self)
        print(self.number)

obj1 = s()
obj2 = r()