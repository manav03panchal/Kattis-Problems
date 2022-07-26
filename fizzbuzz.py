from sys import stdin
fline = stdin.readline()
data = fline.strip().split()
data = [int(i) for i in data]
stuff = list(range(1,data[-1]+1))
for i in range(len(stuff)):
    if stuff[i]%data[0]==0 and stuff[i]%data[1]==0:
        print('FizzBuzz')
    elif stuff[i]%data[0]==0:
        print('Fizz')
    elif stuff[i]%data[1]==0:
        print('Buzz')
    else:
        print(stuff[i]) 