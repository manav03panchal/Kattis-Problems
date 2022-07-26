import random
from sys import stdin
def sumArray(list):
    nlist = []
    for i in range(len(list)):
        nlist.append(sum(list[:i+1]))
    return nlist
def doublesort(n,m):
    Mrange = range(1,m+1)
    RandNums = random.sample(Mrange,n)
    # print(RandNums)
    RandNums.sort()
    # print(RandNums)
    print("{:.2f}".format(sum(RandNums)/len(RandNums)))
    RandNums2 = []
    RandNums2.append(RandNums[0])
    for i in range(0,len(RandNums)-1):
        RandNums2.append(RandNums[i+1]-RandNums[i])
    # print(RandNums2)
    RandNums2.sort()
    print("{:.2f}".format(sum(RandNums2)/len(RandNums2)))
    # print(RandNums2)
    RandNums3 = sumArray(RandNums2)
    # print(RandNums3)
    print("{:.2f}".format(sum(RandNums3)/len(RandNums3)))
f = open('1.txt','r')
fline = f.readline().strip().split()
fline = [int(i) for i in fline]
doublesort(fline[0],fline[1])