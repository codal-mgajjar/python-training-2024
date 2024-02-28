# List
print([x if x in "aeiou" else "*" for x in "hello world"])

# Lambda
str_upper = lambda str: str.upper()
print(str_upper("hello"))

# Map
# with lambda
l1 = list(map(lambda a: a * a, range(1, 10)))
print(l1)

# without lambda
l2 = list(map(len, ["hello", "world"]))
print(l2)

# filter
# with lambda
print([i for i in filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])

# without lambda
def f(i):
    if i > 5:
        return i


print([i for i in filter(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])

# reduce
# reduce with lambda

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))

# reduce without lambda
def addition(x, y):
    return x + y


print(reduce(addition, [1, 2, 3, 4, 5, 6]))

# sorted
# sorted with lambda
l2 = lambda l: sorted(l)
print(l2([4, 2, 1, 5, 2, 1, 4]))

# sorted without lambda
print(sorted([4, 6, 3, 2, 1]))

# Map - Map function takes 2 arguments, one as function to be applied and another as list on which to be applied. It returns map object.
# Filter - Filter function takes 2 arguments, one as function which returns true and false and another list on which the fuction to be applied. It returns filter object.
# Reduce - Reduce function takes 2 arguments, one as function to be used and other as list, it uses all elements of list cumulatively. It returns only single output.
# sorted - Sorted fuction is used to sort elements of tuple, list, set and dictionary which returns list as an output.
