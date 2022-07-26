from sys import stdin
fline = stdin.readline().strip()
if '555' in fline[:3]:
    print(1)
else:
    print(0)