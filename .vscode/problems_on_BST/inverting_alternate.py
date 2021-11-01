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
    
    def printing_left_view(self,node):
        q1=deque()
        q1.append(node)
        while q1:
            l1=len(q1)
            level_el=None
            while l1>0:
                q2=q1.popleft()
                if level_el is None:
                    level_el=q2.data
                    print(level_el,end="->")
                if q2.left:
                    q1.append(q2.left)
                if q2.right:
                    q1.append(q2.right)
                l1=l1-1    
    
    def printing_right_view(self,node):
        q1=deque()
        q1.append(node)
        while q1:
            l1=len(q1)
            level_el=None
            while l1>0:
                q2=q1.popleft()
                if level_el is None:
                    level_el=q2.data
                    print(level_el,end="->")
                if q2.right:
                    q1.append(q2.right)
                if q2.left:
                    q1.append(q2.left)
                l1=l1-1 
    
    def print_bottom(self,node,dist,level,dict):
        if node is None:
            return
        if not dist in dict or level>=dict[dist][1]:
            dict[dist]=(level,node.data)
        if node.left:
            self.print_bottom(node.left,dist-1,level+1,dict)   
        if node.right:
            self.print_bottom(node.right,dist+1,level+1,dict)
            
    def printing_bottom_view(self,node):
        dict={}
        self.print_bottom(node,0,0,dict)
        
        for i in dict.keys():
            print(dict[i][1],end="-")
    
    def print_top(self,node,dist,level,dict):
        if dist not in dict or level<=dict[dist][0]:
            dict[dist]=(level,node.data)
        if node.left:
            self.print_top(node.left,dist-1,level+1,dict)   
        if node.right:
            self.print_top(node.right,dist+1,level+1,dict)    
    
    def printing_top_view(self,node):
        dict={}
        self.print_top(node,0,0,dict)
        for i in dict.keys():
            print(dict[i][1],end="-")
    
    
    
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
    
    def print_K_sum():
        node=self.root
        
        def inorder1(node,k):
            if node is None:
                return 0    
            if k<=0:
                return 0 
            if node.left:
                sum=inorder1(node.left,k)
            if k<=0:
                return sum
            sum=sum+node.data
            k=k-1
            if node.right:
                return sum+inorder1(node.right,k)    
        return inorder1(node,4)        
t1 = BinaryTree(1)
t1.root.left = Node(2)
t1.root.right = Node(3)
t1.root.left.left = Node(4)
t1.root.left.right = Node(5)
t1.root.right.left = Node(6)
t1.root.right.right = Node(7)
t1.print_K_sum()
# t1.root.left.left.left = Node(8)
# t1.root.left.left.right = Node(9)
# t1.root.left.right.left = Node(10)
# t1.root.left.right.right = Node(11)
# t1.root.right.left.left = Node(12)
# t1.root.right.left.right = Node(13)
# t1.root.right.right.left = Node(14)
# t1.root.right.right.right = Node(15)
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
# t1.preOrder(t1.root)
# print('/n')
# t1.inverting_Alternate_level(t1.root)
# t1.preOrder(t1.root)

# t1.printing_left_view(t1.root)
# print('\n')
# t1.printing_right_view(t1.root)
# t1.printing_bottom_view(t1.root)
# print('\n')
# t1.printing_top_view(t1.root)

