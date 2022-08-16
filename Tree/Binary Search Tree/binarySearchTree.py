class Node:
    def __init__(self, val_):
        self.val = val_
        self.right = None
        self.left = None

root = None

def searchValue(node, key):
    
    if node is None:
        return Node(None)
    if node.val == key:
        return node

    if key > node.val:
        return searchValue(node.right, key)
    else:
        return searchValue(node.left, key)


def insertNode(node, keyVal):
    if node is None:
        # if the node is empty, then we will create the root node
        root = Node(keyVal)
        return root
    else: 
        if keyVal > node.val:   # the value will be inserted right, if greater
            node.right = insertNode(node.right, keyVal)
        else:                   # the value will be inserted left, if equal or smaller
            node.left = insertNode(node.left, keyVal)

    return node

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.val)
        inorder(node.right)

def findMin(node):
    if node.left is None:
        return node
    
    return findMin(node.left)

def findMax(node):
    if node.right is None:
        return node
    
    return findMax(node.right)

root = insertNode(root, 5)
root = insertNode(root, 6)
root = insertNode(root, 2)
root = insertNode(root, 10)
root = insertNode(root, 25)
root = insertNode(root, 1)
root = insertNode(root, 4)
inorder(root)

# finding the required node
searchNumber = 20
requiredNode = searchValue(root, searchNumber)
searchNumber = 10
requiredNode = searchValue(root, searchNumber)

print(f"The required value is: {requiredNode.val} at address {requiredNode}" \
        if requiredNode.val else f"Value {searchNumber} not Found")

minValue = findMin(root)
maxValue = findMax(root)
print(f"Min Value: {minValue.val}, Max Value: {maxValue.val}")