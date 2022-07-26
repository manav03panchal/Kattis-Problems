from sys import stdin
fline=stdin.readline().strip()
newline=fline.split('()')
newline=list(set(newline))
if len(newline)==1:
    print('correct')
else:
    print('fix')