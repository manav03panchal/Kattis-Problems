from sys import stdin

flines = stdin.readlines()

input = [i.strip() for i in flines]
count = input[0]
input = input[1:]
output = []
i = 0
while i< int(count):
    output.append(input[i])
    i+=2
for i in range(len(output)):
    print(output[i])
