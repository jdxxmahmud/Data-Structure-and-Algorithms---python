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
        if self.head is None:
            temp = Node(val)
            self.head = temp
            self.tail = temp
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode

    def insert(self, position, val):
        currentPosition = 0
        if position == 1:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return
        if self.head is None:
            self.append(val)
        else:
            currentNode = self.head
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
