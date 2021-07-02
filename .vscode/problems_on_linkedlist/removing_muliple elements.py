class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
        
class linkedlist:
    def __init__(self,):
        self.head=None
    def printing_linkedlist(self):
        if self.head is None:
            return
        temp=self.head
        while temp!=None:
            print(temp.val,end="->")
            temp=temp.next
    def adding_node(self,data):
        n1=Node(data)
        if self.head is None:
            self.head=n1
            return
        temp=self.head 
        while temp.next!=None:
            temp=temp.next
        temp.next=n1  
        return  
                       
    def removing_node(self,val):
        temp=self.head.next
        if self.head is None or val is None:
            return
        prev=self.head
        while temp!=None:
            if temp.val==val:
                prev.next=temp.next
                
            prev=temp
            temp=temp.next    
        if self.head.val==val:self.head=self.head.next
    
                
    def swapping_kth_node(self,k):
        temp=self.head        
        slow=self.head
        fast=self.head
        n=1
        while n<k:
            prev1=fast
            fast=fast.next
            
            n=n+1
        cur1=fast
        print(cur1.val)
        while fast.next:
            prev2=slow
            slow=slow.next
            # print(slow.val)
            fast=fast.next
           
        cur2=slow
        print(cur2.val)
        if cur1==cur2:
            self.head=temp
            self.printing_linkedlist()
            return        
    
    def swapping_nodes(self, n1, n2):
        if self.head is None:
            return None
        cur1 = self.head
        while cur1 and cur1.val != n1:
            prev1 = cur1
            cur1 = cur1.next
        cur2 = self.head
        while cur2 and cur2.val != n2:
            prev2 = cur2
            cur2 = cur2.next
        prev1.next, prev2.next, cur1.next, cur2.next = cur2, cur1, cur2.next, cur1.next            
                        
 
    
        
l1=linkedlist()
l1.adding_node(1)
l1.adding_node(2)
l1.adding_node(3)
l1.adding_node(2)
l1.adding_node(1)
l1.r
# l1.swapping_nodes(3,4)
# l1.swapping_kth_node(3)
# l1.adding_node(6)
# l1.adding_node(6)
# l1.removing_node(6)
# l1.printing_linkedlist()   