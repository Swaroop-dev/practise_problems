class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class doubly_linkedlist:
    def __init__(self):
        self.head=None
    def add_node(self,v1):
        if self.head is None:
            self.head=Node(v1)
        cur=self.head
        while cur.next:
            cur=cur.next                
        cur.next=Node(v1)
        Node(v1).prev=cur 
        
    def printing_list(self):
        cur=self.head
        while cur:
            print(cur.data,end="->")
            cur=cur.next  
            
              
l1=doubly_linkedlist()
l1.add_node(1)           
l1.add_node(2)           
l1.add_node(3)           
l1.add_node(4)           
l1.add_node(5)           
l1.add_node(6)           
l1.printing_list()