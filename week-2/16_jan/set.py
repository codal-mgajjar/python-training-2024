s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 6, 7, 8, 9, 10}

# Intersection
print(s1.intersection(s2))

# Union
print(s1.union(s2))

# diffrence
print(s1.difference(s2))
print(s2.difference(s1))

# symmetric diffrence
print(s1.symmetric_difference(s2))

# superset
print(s1.issuperset(s2))

# subset
print(s1.issubset(s2))

# disjoint check

print(s1.isdisjoint(s2))

# In operator
print(2 in s1)
print(3 not in s2)

# add function
s1.add(7)
print(s1)

# discard function

s1.discard(7)
print(s1)

# remove function
s2.remove(2)
print(s2)

# update
s1.update({4, 6})

# unique elements out of list
l = [2, 4, 5, 5, 3, 1]
s = set(l)
print(s)
