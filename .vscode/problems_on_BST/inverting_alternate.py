# problem:Inverting alternate levels in the binary tree

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left=None
        self.right= None


class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    def levelOrder(self, node):
        q1 = deque()
        q1.append(node)
        while len(q1) > 0:
            n = q1.popleft()
            print(n.data, end="-")
            if n.left:
                q1.append(n.left)
            if n.right:
                q1.append(n.right)    
    
    def preOrder(self,node):
        print(node.data,end="-")
        if node.left:
            self.preOrder(node.left)
        if node.right:
            self.preOrder(node.right)

    def inOrder(self,node):
        if node.left:
            self.inOrder(node.left)
        print(node.data,end="-")
        if node.right:
            self.inOrder(node.right)
            
    def inverting_Alternate_level(self,node):
        q1=deque()
        q1.append(node)
        
        level=False
        level_nodes=deque()
        level_data=deque()
        
        
        while q1:
            size=len(q1)
            for i in reversed(range(size)):
                cur=q1.popleft()
            
                if level:
                    level_nodes.append(cur)
                    level_data.append(cur.data)
                
                if i==0:
                    level=not level
                    while level_nodes:
                        front=level_nodes.popleft()
                        front.data=level_data.pop()
                
                if cur.left:
                    q1.append(cur.left)
                                    
                if cur.right:
                    q1.append(cur.right)
                
        
    def preOrder_iterative(self,node):
        s=deque()
        s.append(node)
        while s:
            n=s.pop()
            print(n.data)
            
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
    
    def inOrder_iterative(self,node):
        s= deque()
        cur=node
        while s or cur:
            if cur:
                s.append(cur)
                cur=cur.left
            else:
                s1=s.pop()
                print(s1.data,end="-")
                cur=s1.right
    
    def spiralOrder(self,node):
        q1=deque()
        q1.append(node)
        flag=True
        while q1:
            if flag:
                level_len=len(q1)
                while level_len>0:
                    cur=q1.popleft()
                    print(cur.data,end="-")
                   
                   
                    if cur.left:
                        q1.append(cur.left)
                    if cur.right:
                        q1.append(cur.right)    
                       
                    level_len=level_len-1
            else:
                level_len=len(q1)
                while level_len>0:
                        cur=q1.pop()
                        print(cur.data,end="-")
                        if cur.right:
                            q1.appendleft(cur.right)
                        if cur.left:
                            q1.appendleft(cur.left)         
                        level_len=level_len-1       
            flag=not flag                                                      
            
    def postOrder_iterative(self,node):    
        s1=deque()
        o1=deque()
        
        s1.append(node)
        while s1:
            cur=s1.pop()
            o1.append(cur.data)
            if cur.left:
                s1.append(cur.left)
            
            if cur.right:
                s1.append(cur.right)
               
        while o1:
            print(o1.pop(),end="-")                 
         

t1 = BinaryTree(1)
t1.root.left = Node(2)
t1.root.right = Node(3)
t1.root.left.left = Node(4)
t1.root.left.right = Node(5)
t1.root.right.left = Node(6)
t1.root.right.right = Node(7)
t1.root.left.left.left = Node(8)
t1.root.left.left.right = Node(9)
t1.root.left.right.left = Node(10)
t1.root.left.right.right = Node(11)
t1.root.right.left.left = Node(12)
t1.root.right.left.right = Node(13)
t1.root.right.right.left = Node(14)
t1.root.right.right.right = Node(15)
# t1.levelOrder(t1.root)
# print("\n")
# t1.preOrder(t1.root)
# print("\n")
# t1.inOrder(t1.root)
# print('\n')
# t1.inverting_Alternate_level(t1.root)
# t1.levelOrder(t1.root)
# print("\n")
# t1.inOrder_iterative(t1.root)
# t1.postOrder_iterative(t1.root)
# print('\n')
# t1.spiralOrder(t1.root)
# print('\n')
t1.preOrder(t1.root)
print('/n')
t1.inverting_Alternate_level(t1.root)
t1.preOrder(t1.root)




