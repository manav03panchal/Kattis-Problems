from sys import stdin

fline = stdin.readline()
theNums = [int(i) for i in fline.split()]
print(theNums[0]*theNums[1]*theNums[2])