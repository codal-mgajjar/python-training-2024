# break statement

i = 0
while i < 7:
    print(i)
    if i == 4:
        print("break")
        break
    i += 1

# continue

for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

# for loop
for i in range(5):
    print(i)

# loop with else

for i in range(3):
    print(i)
else:
    print("done")

# while loop
j = 1
while j < 5:
    print(j)
    j += 1

# pass

while i == j:
    pass
