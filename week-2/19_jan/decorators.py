# Decorators
class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


@decorator
def hello():
    print("hello")


hello()


# addition using decorator
class addDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, a, b):
        result = self.func(a, b)
        print(a)
        print(b)
        return result


@addDecorator
def add(a, b):
    return a + b


add(5, 10)

# time decorator
import time


class timeDec:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(time.time_ns())
        self.func()
        print(("2 second delayed"))


@timeDec
def timeDelay():
    return time.sleep(2)


timeDelay()
