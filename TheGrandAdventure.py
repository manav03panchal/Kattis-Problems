f = open('1.txt','r')
flines = f.readlines()
flines=[i.strip() for i in flines]
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self, someItem):
#         self.stack.append(someItem)
#     def pop(self):
#         self.stack.pop(-1)
#     def isEmpty(self):
#         if len(self.stack)==0:
#             return True
#     def peek(self):
#         return self.stack[-1]
numIters = int(flines[0])
flines.remove(flines[0])
newData=[]
for i in range(len(flines)):
    newData.append(flines[i].replace('.',''))
print(newData)
