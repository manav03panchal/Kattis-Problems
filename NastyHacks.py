from sys import stdin
flines = stdin.readlines()
fdata = [i.strip().split(" ") for i in flines]
numCases = fdata[0]
fdata.remove(fdata[0])
fdata = [[int(i) for i in sublist] for sublist in fdata]
for i in range(len(fdata)):
    if fdata[i][-2]-fdata[i][-1]>fdata[i][0]:
        print('advertise')
    if fdata[i][-2]-fdata[i][-1]==fdata[i][0]:
        print('does not matter')
    if fdata[i][-2]-fdata[i][-1]<fdata[i][0]:
        print('do not advertise')