class Node:
    def __init__(self, val_):
        self.val = val_
        self.next = None


class LL:
    def __init__(self, val_):
        return Node(val_)

    def append(self, val_):
        if self.root is None:
            self.root = LL(val_)

    def print(self):

        while self.root:
            print(self.root.val)
            self.root = self.root.next


root = LL(2)

root.print
