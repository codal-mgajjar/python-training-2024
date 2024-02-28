# find squares
s = [x * x for x in [1, 2, 3, 4]]
print(s)

# upper func
z = [i.upper() for i in ["dfgfg"]]
print(z)

# keep vowels
print([x if x in "aeiou" else "*" for x in "apple"])

# conditional list comprehensions
print([x for x in range(10) if x % 2 == 0])

# dictionary comprehensions
print({x: x * x for x in (1, 2, 3, 4)})
