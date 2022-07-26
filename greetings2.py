from sys import stdin
# f = open('1.txt','r')
fline = list(stdin.readline().strip())
toInsert = fline.count('e')
for i in range(toInsert):
    fline.insert(1,'e')
print(''.join(fline))