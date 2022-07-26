from sys import stdin
flines = stdin.readlines()
flines = [i.split() for i in flines]
fdata = flines[1]
fdata = [int(i) for i in fdata]
print(sum(fdata))