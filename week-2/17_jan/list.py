l1 = [1,2,3,4,5,6]
l2 = [8,9,10]

#append
l1.append(7)
print(l1)

#extend
l1.extend(l2)
print(l1)

#get index of first occurence
print(l1.index(3))

#insert
l1.insert(0,55)
print(l1)

#pop element
print(l1.pop(0))

#remove
l1.remove(6)
print(l1)

#reverse
l2.reverse()
print(l2)

#count
print(l1.count(1))

#sort
l1.sort()

#clear
l2.clear()

#copy
l3 = list(l1)
print(l3)

#check if list is empty
if not l3:
    print('empty')

#iterating list

for i in l3:
    print(i)

for index, item in enumerate(l1):
    print(index, item)

#check if item is in the list

print(6 in l3)

#any and all function
print(all(l3))
print(any(l3))

#merge list
l4  = l1+ l2
