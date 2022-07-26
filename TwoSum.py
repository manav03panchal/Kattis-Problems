from sys import stdin

fline = stdin.readline()
theNums = [int(i) for i in fline.split()]
print(sum(theNums))