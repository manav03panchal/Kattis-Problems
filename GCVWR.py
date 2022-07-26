from sys import stdin
flines = stdin.readlines()
flines = [i.split() for i in flines]
for i in range(len(flines)):
    for j in range(len(flines[i])):
        flines[i][j]=int(flines[i][j])
G = flines[0][0]
T = flines[0][1]
PercentGT = 0.9*(G-T)
SumItems = sum(flines[1])
GCVWR = PercentGT-SumItems
print(int(GCVWR))