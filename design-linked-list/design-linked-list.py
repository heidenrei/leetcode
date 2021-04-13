class Node:
    def __init__(self, val, pre=None, nex=None):
        self.val = val
        self.pre = pre
        self.nex = nex


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        
    def print_ll(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.nex

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #self.print_ll()
        if self.head:
            cnt = 0
            curr = self.head
            while cnt < index and curr.nex:
                curr = curr.nex
                cnt += 1
            return curr.val if (curr and cnt == index) else -1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head:
            new = Node(val, pre=None, nex=self.head)
            self.head.pre = new
            self.head = new
        else:
            self.head = Node(val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head:
            curr = self.head
            while curr.nex:
                curr = curr.nex
            new = Node(val, pre=curr, nex=None)
            curr.nex = new
        else:
            self.head = Node(val)
                
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        cnt = 0
        curr = self.head
        while cnt < index and curr.nex:
            curr = curr.nex
            cnt += 1

        if curr and cnt == index:
            new = Node(val, pre=curr.pre, nex=curr)
            if curr.pre:
                curr.pre.nex = new
            curr.pre = new
        
        elif cnt == index-1 and not curr.nex:
            curr.nex = Node(val, pre=curr)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        self.print_ll()
        print()
        if index == 0 and self.head:
            self.head = self.head.nex
        
        if self.head:
            cnt = 0
            curr = self.head
            while cnt < index and curr.nex:
                curr = curr.nex
                cnt += 1
            if curr.pre and curr.nex and cnt == index:
                curr.pre.nex = curr.nex
                curr.nex.pre = curr.pre
            if not curr.nex and curr.pre and cnt == index:
                curr.pre.nex = None
        self.print_ll()
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)