from sys import stdin
fline = stdin.readline()
theNums = [int(i) for i in fline.split()]
print(round(theNums[0]*min(theNums[1]-1, theNums[1]))+1)