

import numpy as np
array = np.random.randint(1, 100, 10)
bstTree = BST()
for num in array:
    bstTree.insert(num)

print(bstTree.root.val)
