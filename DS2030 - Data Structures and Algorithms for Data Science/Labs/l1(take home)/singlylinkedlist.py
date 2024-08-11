class Node:
    
    # a Node class to store the elements of the Singly Linked List

    def __init__(self, e, n):
        self.element = e
        self.next = n
 
    def getElement(self):
        return self.element

    def getNext(self):
        return self.next
    
    def setNext(self, iNode):
        self.next = iNode


class SLLIterator:
    # making an iterator for the singly liniked lists so that list traversal becomes very easy
    def __init__(self, head):
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        else:
            elem = self.curr
            self.curr = self.curr.next
            return elem
        
class SinglyLinkedList:
    # the singly linked list class that stores the all the nodes

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.setNext(self.tail)
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        return SLLIterator(self.head)

    def isEmpty(self):
        return self._size == 0

    def addFirst(self, elem_val):
        self.head = Node(elem_val, self.head)
        if self._size == 0:
            self.tail = self.head
        # although we initially defined tail to be the next node of head, here we are just making it to be the last element of the linked list, which continues in all the functions that add the elements...
        self._size+=1
    
    def addLast(self, elem_val):
        iNode = Node(elem_val, None)
        if (self.isEmpty()):
            self.head = iNode
        else:
            self.tail.setNext(iNode)
        self.tail = iNode
        self._size += 1

    def add(self, elem_val):
        self.addLast(elem_val)

    def pop(self):
        # I was unable to think of a better way than this to pop the last elelement for a singly linked list, so... I just went with it...
        if self._size == 0:
            return None
        elif self._size == 1:
            self.head = Node(None, None)
            return self.head
        self._size -= 1
        for e in self:
            if e.next == self.tail:
                temp = e.next
                self.tail = e
                e.next = None
                return temp

