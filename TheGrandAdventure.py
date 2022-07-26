class Stack:
    def __init__(self):
        self.stack=[]
    def push(self, someItem):
        self.stack.append(someItem)
    def pop(self):
        self.stack.pop(-1)
    def isEmpty(self):
        if len(self.stack)==0:
            return True
    def peek(self):
        return self.stack[-1]

for i in range(input()):
    pass