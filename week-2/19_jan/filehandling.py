#Open a file
file = open('test.txt', 'r')

#readfile
for r in file:
    print(r)

print(file.read())

#with statement
with open('test.txt') as f:
    print(f.read())

f.close()
#split lines
for lines in file:
    word = lines.split()
    print(word)

#close file
file.close()

#write in file
file = open('test2.txt', 'w')
file.write('Hello, how are you? ')
file.write('welcome to codal')
file.close()

with open('test2.txt') as f:
    for lines in f:
        word = lines.split()
        print(word)
file.close()
f.close()

#append mode
file2 = open('test2.txt', 'a')
file2.write('Thankyou')

file3 = open('test2.txt','r')
print(file3.read())
