from inverting_alternate import Node, BinaryTree
from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to print pre-order traversal of given tree
def preorder(root):
 
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# Recursive function to in-place convert the given binary tree to its
# sum tree by traversing the tree in post-order manner
def convertToSumTree(root):
 
    # base case: tree is empty
    if root is None:
        return 0
 
    # recursively convert left and right subtree first before
    # processing the root node
    left = convertToSumTree(root.left)
    right = convertToSumTree(root.right)
 
    # stores current value of root node
    old = root.data
 
    # update root to sum of left and right subtree
    root.data = left + right
 
    # return the updated value plus old value (sum of tree rooted at root node)
    return root.data + old
 
 
if __name__ == '__main__':
 
  
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    convertToSumTree(root)
    preorder(root)
