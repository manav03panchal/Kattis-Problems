from sys import stdin
lines = stdin.readlines()
info = [int(i.strip()) for i in lines]
data_allowed = info[0]
numMonths = info[1]
# not a series, could be random sequence
info = info[2:]
for i in range(len(info)):
    info[i] = data_allowed - info[i]
print(int(sum(info) + int(data_allowed)))