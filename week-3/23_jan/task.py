# use of seek function
with open("test.txt", "r") as f:
    f.seek(5)
    print(f.read())


# Decorator function way
def dec1(func):
    def dec2(*args, **kwargs):
        r = func()
        print("hello")
        print(r)
        print("bye")

    return dec2


@dec1
def dec3():
    return "temp text"


dec3()
print(dec3.__name__)
print(dec3.__doc__)


# decorator class way
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


# wraps function for metadata
from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)
print(f.__doc__)
