class a:
    static_var = 5

    def __init__(self) -> None:
        a.static_var += 1
        self.instance_var = a.static_var

obj1 = a()
print(a.static_var,obj1.instance_var)
obj2 = a()
print(a.static_var,obj2.instance_var)
