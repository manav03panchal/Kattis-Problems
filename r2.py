from sys import stdin

fline = stdin.readline().split()
input = [int(i) for i in fline]
S = input[1]
r1 = input[0]
r2 = 2*S-r1
print(r2)