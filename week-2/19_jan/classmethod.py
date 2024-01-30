class student:
    def __init__(self,firstname,surname):
        self.firstname = firstname
        self.surname = surname
        self.nickname = None

    def set_nickname(self, name):
        self.nickname = name

    @classmethod
    def getname(cls,name: str):
        firstname, lastname = name.split()
        return student(firstname,lastname)

obj = student.getname("meshw gajjar")
print(obj.firstname)
print(obj.surname)

#another example

class employee:
    company = "codal"
    def show(self):
        self.name = "gajjar"
        print(f"Name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = employee()
e1.name = "Meshw"
e1.show()
e1.changeCompany("codal2")
e1.show()
print(employee.company)

