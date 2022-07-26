from sys import stdin
# f = open('1.txt','r')
flines = stdin.readlines()
fdata = [i.strip() for i in flines]
fdata.pop(0)
fdataMod = [i.split() for i in fdata]
for i in range(len(fdataMod)):
    if 60/int(fdataMod[i][0])<=10:
        print(f'{"{0:.4f}".format(60)} {"{0:.4f}".format(60*float(fdataMod[i][0])/float(fdataMod[i][1]))} {"{0:.4f}".format(60*float(fdataMod[i][0])/float(fdataMod[i][1])+60/float(fdataMod[i][1]),4)}')
    else:
        print(f'{"{0:.4f}".format(60/float(fdataMod[i][1]))} {"{0:.4f}".format(60*float(fdataMod[i][0])/float(fdataMod[i][1]))} {"{0:.4f}".format(60*float(fdataMod[i][0])/float(fdataMod[i][1])+60/float(fdataMod[i][1]))}')

        