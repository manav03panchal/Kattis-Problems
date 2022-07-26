from sys import stdin

flines = stdin.readlines()
input = [str(i.strip()) for i in flines]
stuff1 = []
stuff2 = []
singleStuff = []
for i in range(len(input)):
    if len(input[i]) == 1:
        input[i]+='0'
        singleStuff.append(1)
    stuff2.append(input[i][-1])
    stuff1.append(input[i][:-1])
crap = []
for i in range(len(stuff1)):
    crap.append(int(stuff1[i])**int(stuff2[i]))
print(sum(crap)-sum(singleStuff))