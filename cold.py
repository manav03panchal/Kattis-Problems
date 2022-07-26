from sys import stdin
flines = stdin.readlines()
fdata = [str(i).strip() for i in flines]
data = fdata[1].split()
data = [int(i) for i in data]
output = []
for i in range(len(data)):
    if data[i]<0:
        output.append(i)
print(len(output))
