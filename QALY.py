from sys import stdin

flines = stdin.readlines()
info = [i.strip().split() for i in flines]
info = sum(info,[])
info = [float(i) for i in info]
count = info[0]
info = info[1:]
prod = []
i = 0
while i<=count*2-2:
    prod.append(info[i]*info[i+1])
    i+=2

print(sum(prod))