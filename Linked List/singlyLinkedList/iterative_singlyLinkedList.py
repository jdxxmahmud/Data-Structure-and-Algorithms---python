class Node:
    def __init__(self, val_):
        self.val = val_
        self.next = None

class LinkedList:
    def insertNode(root, val_):
        if root is None:
            return Node(val_)
        currentNode = root
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(val_)
        return root

    def printNodes(root):
        while root:
            print(root.val)
            root = root.next

root = None
root = LinkedList.insertNode(root, 2)
root = LinkedList.insertNode(root, 4)
root = LinkedList.insertNode(root, 10)
root = LinkedList.insertNode(root, 12)
root = LinkedList.insertNode(root, -1)
root = LinkedList.insertNode(root, 0)
LinkedList.printNodes(root)