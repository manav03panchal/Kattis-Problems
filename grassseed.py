from sys import stdin
flines = stdin.readlines()
fdata = [i.strip().split() for i in flines]
cost = float(''.join(fdata.pop(0)))
fdataMod =[[float(i) for i in sublist] for sublist in fdata]
fdataMod.pop(0)
sumOutput = []
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result
for i in range(len(fdataMod)):
    sumOutput.append((multiplyList(fdataMod[i]))*cost)
print('{0:.6f}'.format(sum(sumOutput)))