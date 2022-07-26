from sys import stdin
lines = stdin.readline()
lines = int(lines.strip())
if lines%2 == 0:
    print('Bob')
else:
    print('Alice')