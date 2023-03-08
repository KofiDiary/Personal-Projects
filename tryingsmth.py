file = open('file.txt.txt', 'w')

file.write ('Sing\n')
file.write ('Dance\n')
file.write ('Walk\n')

print (file)

file.close()

file = open('file.txt.txt', 'r')
f = file.readlines()

newList = []
for line in f:
    if line [-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print (newList)

file.close()
