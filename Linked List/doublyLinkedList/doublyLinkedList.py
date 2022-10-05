from more_itertools import tail


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node

    def printList(self):

        temp = self.head
        print("The elements of the list are:", end=" ")
        while temp:
            print(f"{temp.val} => ", end=" ")
            temp = temp.next

    def append(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = tail

        self.tail = newNode
        
        # Returning true
        # so that this can be
        # used in other node
        return True
    
    def pop(self):
        
        if self.head is None:
            return None
        elif self.head == self.tail:
            poppedNode = self.head
            self.head = None
            self.tail = None
        else:
            poppedNode = self.tail
            self.tail = self.tail.prev
            self.tail.next = Node
            poppedNode.prev = None
            
        return poppedNode   
    
        
    


myDLL = DoublyLinkedList(15)
myDLL.append(10)
myDLL.append(5)
myDLL.append(1)
myDLL.append(127)
myDLL.append(-12)
myDLL.printList()
print(f"\n Tail: {myDLL.tail.val}")
