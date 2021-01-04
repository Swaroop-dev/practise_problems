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

    def printing_node(self):
        if self.head is None:
            return None
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def reversing_linkedlist(self):
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

    def deleting_node(self, n1):
        if self.head is None:
            return None
        cur = self.head
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

    def reversing_part_of_the_linkedlist(self, index1, index2):
        cur = self.head
        inc = 1
        while cur and inc <index1:
            prev = cur
            cur = cur.next
            inc = inc+1
        s1=prev
        s2=cur    
        while cur and inc <= index2:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            inc = inc+1
        s1.next=prev 
        s2.next=cur 

    


l1 = linkedlist()
l1.adding_node(1)
l1.adding_node(2)
l1.adding_node(3)
l1.adding_node(4)
l1.adding_node(5)
l1.adding_node(6)
l1.reversing_part_of_the_linkedlist(2, 5)
l1.printing_node()
