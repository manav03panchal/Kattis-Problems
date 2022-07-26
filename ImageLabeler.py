f = open('1.txt','r')
flines = f.readlines()
fdata = [i.split() for i in flines]
fcases = int(fdata[1][1])
fnums = fdata[2]
print(fnums)
print(fcases)
fnums = [int(i) for i in fnums]
fnums.sort()
def findMedian(list):
    if len(list)%2 == 0:
        return float(list[len(list)//2]+list[(len(list)-1)//2])/2
    else:
        return float(list[len(list)//2])
if fcases == 1:
    print(findMedian(fnums))
else:
    print(findMedian(fnums[:fcases]) + sum(fnums[fcases:]))
