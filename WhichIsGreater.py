from sys import stdin

fline = stdin.readline()
theNums = [int(i) for i in fline.split()]

if theNums[0]>theNums[1]:
    print(1)
else:
    print(0)