t = ("a", "b", "c", "d")


# create single value tuple

t1 = ("a",)
print(type(t1))

# range in tuple

trange = tuple(range(5))
print(trange)

# Length, min, max of tuple
print(len(t))
print(max(t))
print(min(t))

# tuple concatenation

print(t + t1)

# tuple indexing
print(t[0])
print(t[::-1])
print(tuple(reversed(t)))
