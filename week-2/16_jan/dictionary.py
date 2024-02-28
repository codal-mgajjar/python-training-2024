d1 = {1:'a', 2:'b', 3:'c'}


#making copy of dictionary
d2={**d1}
print(d2)

#adding new key and value
d1[4] = 'd'
print(d1)

#modifying value
d1[4] = 'e'
print(d1)

#delete key value
del d1[4]

# avoiding keyerror
print(d1.get(7, 'Nothing'))
print(d1.setdefault(1, 'g'))

# iterating over dictionary
for key, value in d1.items():
    print(key, value)



#Merging dictionaries
d2 = {9:'z'}
d3 = {**d1, **d2}
print(d3)


#accessing keys and values
print(d1.keys())
print(d1.values())
print(d1.items())

#default dictionary
from collections import defaultdict
dd = defaultdict(int)
dd['keys']
dd['key'] = 1
print(dd)


#creating ordered dictionary
from collections import OrderedDict
dz = OrderedDict()
dz['first'] = 1
dz['second'] = 2

print(dz)
