from sys import stdin

lines = stdin.readlines()
coordinates = [int(i.strip()) for i in lines]



if coordinates[0]*coordinates[1] > 0:
    if coordinates[0] < 0:
        print('3')
    else:
        print('1')

if coordinates[0]*coordinates[1] < 0:
    if coordinates[0]<0:
        print('2')
    else:
        print('4')