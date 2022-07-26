from sys import stdin
flines = stdin.readlines()
fdata = [int(i.strip())for i in flines]
fdata.remove(fdata[0])
print(sum(fdata)-len(fdata)+1)