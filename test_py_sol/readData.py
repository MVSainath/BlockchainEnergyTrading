file = open('data.txt', 'r')
read = file.readlines()

modified = []

for line in read:
    if line not in modified:
        modified.append(line.strip())
    '''if line[-1] == '\n':
        modified.append(line[:-1])
    else:
        modified.append(line)'''

print(read)
print(modified)