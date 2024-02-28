def dec_with_arg1(argument):
    def timer1(func):
        print("timer1 run")

        def wrapper_func1():
            print(f"{argument}")
            func()
            return 0

        return wrapper_func1

    return timer1


def dec_with_arg2(argument):
    def timer2(func):
        print("timer2 run")

        def wrapper_func2():
            print(f"{argument}")
            func()
            return 0

        return wrapper_func2

    return timer2


# decorator stacking
@dec_with_arg2("Welcome")
@dec_with_arg1("Bye")  # hellofunc = dec_with_arg1(hellofunc)
def hello_func():
    print("Hello")


hello_func()
