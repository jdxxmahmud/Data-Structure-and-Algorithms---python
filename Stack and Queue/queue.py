class Node:
    def __init__(self, val):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, val):
        newNode = Node(val)
        self.first = newNode
        self.last = newNode

    def print_queue(self):
        temp = self.first

        while temp:
            print(f"{temp.val} => ", end=" ")
            temp = temp.next

    def enque(self, val):
        pass
    
    def deque(self, val):
        pass