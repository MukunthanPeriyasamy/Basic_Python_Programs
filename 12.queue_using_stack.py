class Queue_using_stack:
    
    def __init__(self):
        self.st1=[] # Primary Stack 
        self.st2=[] # Scondary Stack
    
    def enqueue(self,val):
        self.st1.append(val)
    def dequeue(self):
        # Moving all the values except the last(bottom of the satck) value from the stack1 to stack2
        while len(self.st1) > 1:
            val = self.st1.pop()
            self.st2.append(val)
            
        self.st1.pop()
        
        # Moving all the values value from the stack2 to stack1
        while len(self.st2) >  0:
            val = self.st2.pop()
            self.st1.append(val)
    def print_queue(self):
        print(" ".join(map(str,self.st1)))
        
queue = Queue_using_stack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.print_queue()

queue.dequeue()
queue.print_queue()

queue.dequeue()
queue.print_queue()

