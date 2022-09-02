class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    head = None
    tail = None

    def __init__(self, val=None):
        # if no value is given, an empty linked list will be initialized
        self.head = Node(val) if val else None
        self.tail = self.head

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
            return

        print("The elements are:", end=" ")
        temp = self.head

        while temp:
            print(temp.val, end=" => ")
            temp = temp.next
        print()

    def append(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode

        self.tail = newNode

    def findLength(self):
        currentLength = 0
        currentNode = self.head
        while currentNode:
            currentLength += 1
            currentNode = currentNode.next
        return currentLength

    def insert(self, position, val):
        if position < 0:
            print("Index starts at 0")
        elif position > self.findLength():
            print("Exceeds index limit")
        elif position == 1:
            return self.insertFirst(val)
        elif position == self.findLength():
            return self.append(val)
        else:
            currentNode = self.head
            currentPosition = 0

            # This loop will run upto the previous node of the
            #   expected position
            while currentNode.next:
                newNode = Node(val)
                currentNode = currentNode.next
                currentPosition += 1
                if currentPosition == position - 1:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    return

    def pop(self):

        prevNode = self.head

        if self.head is self.tail:
            self.head = self.tail = None
            return prevNode
        currentNode = self.head

        while currentNode.next:
            prevNode = currentNode
            currentNode = currentNode.next

        prevNode.next = None
        self.tail = prevNode

        return currentNode

    def insertFirst(self, val):
        newNode = Node(val)

        if self.head is None:
            self.tail = newNode
        else:
            newNode.next = self.head

        self.head = newNode

    def popFirst(self):
        if self.head is None:
            print("Linked List empty, can not pop")
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next or None
            return poppedNode

    def remove(self, val):
        if self.head.val == val:
            return self.popFirst()

        prevNode = self.head
        currentNode = self.head
        while currentNode.next:
            if currentNode.val == val:
                deletedNode = currentNode
                prevNode.next = currentNode.next
                return deletedNode
            prevNode = currentNode
            currentNode = currentNode.next

        print("Value not found")
        return None


myLL = LinkedList()
myLL.append(5)
myLL.append(2)
myLL.append(6)
myLL.append(7)
myLL.append(1)

myLL.printList()
poppedNode = myLL.popFirst()
print(f"Popped Node: {poppedNode.val}")
deletedNode = myLL.remove(6)
print(f"Deleted: {deletedNode.val}" or "Failed")

deletedNode = myLL.remove(2)
print(f"Deleted: {deletedNode.val}" or "Failed")
myLL.printList()
