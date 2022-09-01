class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    head = None
    tail = None

    def __init__(self, val):
        self.head = Node(val)
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
        if position == 1:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return
        if self.head is not None:
            currentNode = self.head
            currentPosition = 0
            while currentNode is not None:
                if currentPosition == position - 2:
                    newNode = Node(val)
                    newNode.next = currentNode.next
                    currentNode.next = newNode

                    return

                currentPosition += 1
                currentNode = currentNode.next

            print("Not that many elements, so appending")
            self.append(val)


myLL = LinkedList(5)
myLL.append(6)
print("Tail: ", myLL.tail.val)
myLL.append(10)
print("Tail: ", myLL.tail.val)
myLL.printList()
myLL.insert(3, 20)
myLL.printList()
myLL.insert(100, 3)
myLL.printList()
print("Tail: ", myLL.tail.val)
myLL.insert(1, 125)
myLL.printList()
print("Head: ", myLL.head.val)

print(f"Current length of linked list is: {myLL.findLength()}")
