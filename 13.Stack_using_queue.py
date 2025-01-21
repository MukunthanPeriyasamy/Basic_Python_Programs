from collections import deque
class Stack_using_queue:
    
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self,val):
        self.q2.append(val)
        
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1,self.q2 = self.q2,self.q1
        
    def pop(self):
        if self.q1:
            self.q1.popleft()
        else:
            print("Stack is empty")
    def print_stack(self):
        print(" ".join(map(str,self.q1)))
    
stack = Stack_using_queue()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print_stack()

stack.pop()
stack.print_stack()

print(int(eval("7 + ( 4 - 5)")))