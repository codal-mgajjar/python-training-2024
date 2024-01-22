#Class
class a:
    pass

#object
obj = a()

#__init__ method
class abc:
    
    def __init__(self, name) -> None:
        self.name = name
        print(self.name)

    def speak(self):
        print(f"hello I'm {self.name}")


o1 = abc("meshw")
o1.speak()
print(o1.name)


#__str__ method
class xyz:
    
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"My name is {self.name}"
    
o2 = xyz("meshw")
print(o2)

#global, class and instance variable
animal = "cow"
class ci:
    #class variable
    animal = "Dog"
    def __init__(self,color) -> None:
        #instance variable
        self.color = color
    
ci_obj = ci("black")
print(animal)
print(f"{ci_obj.animal} is {ci_obj.color} in color")


#default constructor
class default_cons:
    def __init__(self) -> None:
        self.name = "meshw"

    def printname(self):
        return f"I'm {self.name}"
dc_obj = default_cons()
print(dc_obj.printname())

#parameterized constructor

class parameterized_cons:
    
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        print(f"hello I'm {self.name}")

p_obj = parameterized_cons("meshw")
p_obj.speak()

#Both constructors

class both_cons:
    
    def __init__(self, name=None) -> None:
        self.name = name

    def speak(self):
        if self.name == None:
            print("Nothing")
        else:
            print(f" I'm {self.name}")

pb_obj = both_cons()
pb_obj.speak()

#destructor
class employee:
    def __init__(self) -> None:
        print("Constructor called")
    
    def ez(self):
        print("function called")

    def __del__(self):
        print("destructor called")

obj = employee()
del obj
obj.ez()