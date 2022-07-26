from sys import stdin
flines = stdin.readlines()
flines=[i.split() for i in flines]
for i in range(len(flines)):
    for j in range(len(flines[i])):
        flines[i][j]=int(flines[i][j])
numTestCases=flines[0][0]
for i in range(numTestCases):
    print(sum(flines[i+1][1:])-(flines[i+1][0]-1))