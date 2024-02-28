# String

s1 = "abcdefg"
s2 = "abcdefg"
print(s1)
print(s2)
print(s1[0])
print(s2[0:3])
print(s1[::-1])
print(s2[0:4:2])
print(type(s1))

# numbers

int_num = 10
float_num = 1.4
complex_num = 2.4j

print(type(complex_num))

print(int_num)
print(float_num)
print(complex_num)


# Sets

set1 = {"apple", "banana", "cake"}
print(set1)
set1.add("orange")
print(set1)

# Frozenset

f1 = {"kdeof", "deddwdw", "wdwddqd"}
f2 = frozenset(f1)
f3 = frozenset(["jdsifjd", "ejfefhi"])
print(f3)


# Lists

l1 = ["sdksdiv", "dkidve", "a", "a", 123]
l2 = [3, "efef"]
print(l1)
print(l1[0])
print(l1[::-1])
print(l1 * 2)
print(l1 + l2)

# tuple

t1 = (123, "dsdsd")
print(t1[0])
print(t1 + tuple("3442"))


# dictionary

d1 = {12: "djfijsf", 1: "dsfd"}
print(d1)
print(d1[12])
print(d1.keys())
print(d1.values())


# boolean

b1 = True
print(type(b1))


# nonetype

n = None
print(type(n))


# bytes

bb = b"hello"
print(bb)
print(type(bb))
print(bb.decode())


# Range

r = range(5)
print(r)
