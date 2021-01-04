# contruction of btree using levelorder and preorder
# contruction of btree using inorder and preorder
# contruction of btree using postorder and preorder
# contruction of btree using postorder and inorder


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printing_tree(node):
    if node is None:
        return
    print(node.data, end="->")
    if node.left:
        printing_tree(node.left)
    if node.right:
        printing_tree(node.right)


def createTree(start, end1, d, inorder):
    if start > end1:
        return None

    index = start

    for j in range(start+1, end1+1):
        if d.get(inorder[j]) < d.get(inorder[index]):
            index = j
    print(index, start, end1,end="-")
    root = Node(inorder[index])
    root.left = createTree(0, index-1, d, inorder)
    root.right = createTree(index+1, end1, d, inorder)
    print(root.data)
    return root


def tree_const_using_pre_level(inorder, level):
    d1 = dict()
    for i, e in enumerate(level):
        d1[e] = i
    return createTree(0, len(inorder)-1, d1, inorder)


t1 = tree_const_using_pre_level([4, 2, 5, 1, 6, 3, 7], [1, 2, 3, 4, 5, 6, 7])
print(t1.right.data)
printing_tree(t1)
