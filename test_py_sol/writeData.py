file = open("data.txt","w")

data = []
arrayLength = int(input())
for i in range (arrayLength):
    values = int(input())
    data.append(values)
    file.write(str(values) + '\n')

print(data)
file.close()
