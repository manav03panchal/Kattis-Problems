from sys import stdin
fline = stdin.readline().strip()
for i in range(len(fline)):
    if fline[i] == 'a':
        break
print(fline[i:])