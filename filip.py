from sys import stdin
fline = stdin.readline().split()
fline = [int(i[::-1]) for i in fline]
fline.sort()
print(fline[-1])