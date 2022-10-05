class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class Stack:
    def __init__(self, val):
        newNode = Node(val)
        self.top = newNode
        
    def print_stack(self):
        temp = self.top
        while temp:
            print(f"{temp.val} => ", end = " ")
            temp = temp.next
            
    def push(self):
        pass
    
    def pop(self):
        pass
    