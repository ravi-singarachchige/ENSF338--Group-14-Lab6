import timeit
import random
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return
        
        currentNode = self.root
        while True:
            if key < currentNode.val:
                if currentNode.left is None:
                    currentNode.left = Node(key)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = Node(key)
                    break
                else:
                    currentNode = currentNode.right

    def search(self, key):
        currentNode = self.root
        while currentNode:
            if key == currentNode.val:
                return True  # Found the key
            elif key < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False  # Key not found

# Example usage
bst = BST()

# Insert elements into the BST
for item in range(1, 10001):  # Simulating insertion of a sorted list
    bst.insert(item)

# Search for some elements
print(bst.search(500))  # True
print(bst.search(10001))  # False


# The iterative approach is generally faster and more memory-efficient for large
# datasets because it avoids the overhead associated with the call stack in recursion.
# Recursive approaches can lead to stack overflow errors for deeply nested operations 
# (like inserting into a highly unbalanced tree), while iterative solutions maintain
# a constant stack size, making them more robust for operations on large datasets.