class a:
    def __init__(self):
        self.name = "max"
        self._age = 21
        self.__number = 1


class b(a):
    def __init__(self):
        a.__init__(self)
        print(self.name)
        print(self._age)


#        print(self.__number)

obj = b()
