#reversing the linked list
#rerversing the part of linked list
#circular deletion of nodes
#folding of linked list
#swapping the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def adding_node(self, n1):
        if self.head is None:
            self.head = Node(n1)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(n1)

    def printing_node(self,n1=None):
        
        if n1 is None:
            if self.head is None:
                return None
            cur = self.head
            while cur:
                print(cur.data, end="->")
                cur = cur.next
            return 
        cur=n1
        while cur:
            print(cur.data,end="->")
            cur=cur.next
            
        

    def reversing_linkedlist(self,n1=None):
        if n1 is None:
            if self.head is None:
                return None
            cur = self.head
            prev = None

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            self.head = prev
            return
        cur=n1
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev    

    def deleting_node(self, n1):
        if self.head is None:
            return None
        cur = self.head
        if self.head.data == n1:
            nxt = self.head.next
            self.head.next = None
            self.head = nxt
            return
        while cur and cur.data != n1:
            prev = cur
            cur = cur.next
        if cur is None:
            return None
        prev.next = cur.next
        cur = None

    def swapping_nodes(self, n1, n2):
        if self.head is None:
            return None
        cur1 = self.head
        while cur1 and cur1.data != n1:
            prev1 = cur1
            cur1 = cur1.next
        cur2 = self.head
        while cur2 and cur2.data != n2:
            prev2 = cur2
            cur2 = cur2.next
        prev1.next, prev2.next, cur1.next, cur2.next = cur2, cur1, cur2.next, cur1.next

    def deleting_mid_element(self):
        if not self.head:
            return
        while self.head:
            cur1 = cur2 = self.head
            prev = None
            while cur2 and cur2.next:
                prev = cur1
                cur1 = cur1.next
                cur2 = cur2.next.next
                
            if cur1 == self.head:
                self.head = None
                print("List empty")
                return
            prev.next = cur1.next
            cur1.next = None
            self.printing_node()
            print('\n')
    
    def folding_the_linked_list(self):
        #steps to solve
        #find the middle element
        #slit into ll
        #reverse the second split
        #merge them

        cur=self.head
        slow=fast=cur
        while fast and fast.next:
            prev = slow
            slow=slow.next
            fast=fast.next.next  
        print(slow.data) 
        temp=prev.next    
        prev.next=None
        self.printing_node(n1=temp)
        print('\n')
        self.printing_node()
        print('\n')
        #reversing list
        first=self.head
        second=self.reversing_linkedlist(n1=temp)
        self.printing_node(n1=second)
        print('\n')
        #merging the linked list
        while second.next:
            temp=first.next
            first.next=second
            first=temp
            temp=second.next
            second.next=first
            second=temp 
        self.adding_node(second.data)       
        self.printing_node()    
           
    
    def finding_the_intersection(self,l):
        cur1=self.head
        cur2=l.head
        while cur1 and cur2:
            if cur1==cur2:
               print(cur1.data)
               return 
            cur1=cur1.next     
            cur2=cur2.next     
        return
    
    def reversing_part_of_the_linkedlist(self, index1, index2):
        cur = self.head
        inc = 1
        prev = None
        while cur and inc < index1:
            prev = cur
            cur = cur.next
            inc = inc+1
        s1 = prev
        s2 = cur
        while cur and inc <= index2:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            inc = inc+1
        s1.next = prev
        s2.next = cur


l1 = linkedlist()
l2=linkedlist()
l2.adding_node(2)
l2.adding_node(3)
l2.adding_node(4)
l2.adding_node(1)
l2.adding_node(5)
l2.adding_node(9)
l2.adding_node(8)
l1.adding_node(1)
l1.adding_node(2)
l1.adding_node(3)
l1.adding_node(4)
l1.adding_node(5)
l1.adding_node(6)
l1.adding_node(7)
l1.adding_node(8)
# l1.folding_the_linked_list()
l1.finding_the_intersection(l2)
# l1.printing_node()
# print('\n')
# l1.deleting_mid_element()
# l1.reversing_part_of_the_linkedlist(2, 5)
# print('\n')
# l1.printing_node()
