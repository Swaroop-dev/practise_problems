class Node:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev=prev
        self.next=next

class Queue:
    def __init__(self):
        self.head=None
        self.last=None
        
    def enqueue(self,val):
        n1=Node(val)
        if self.last is None:
            self.last=self.head=n1
            return
        self.last.next=n1
        n1.prev=self.last
        self.last=self.last.next
        return    
    
    def deqeue(self,val):
        if self.head is None:
            return
        self.head=self.head.next
        self.head.prev=None
        return 
    
    def isEmpty(self):
        if self.last is None:
            return True
        cur=self.head
        cnt=1
        while cur!=self.last:
            cur=cur.next 
            cnt=cnt+1
        return cnt                   
        