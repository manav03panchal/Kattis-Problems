from sys import stdin

fline = stdin.readline()
theNums = [int(i) for i in fline.split()]
print(0.5*(theNums[0]*theNums[1]))