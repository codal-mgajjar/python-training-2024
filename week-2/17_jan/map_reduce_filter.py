#map function 
def square(a):
    return a * a 
b = list(map(square, range(1, 5)))
print(b)


#length func
l = list(map(len, ['rdgr','rgrgdfds']))
print(l)

#filter function

arr = [1,2,3,4,5,6]
print([i for i in filter(lambda x: x>4, arr)])


from functools import reduce
#reduce function 

print(reduce(lambda x, y : x + y, [1,2,3,4,5,6]))