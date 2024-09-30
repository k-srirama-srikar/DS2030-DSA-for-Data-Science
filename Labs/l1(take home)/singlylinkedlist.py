class Node:
    
    # a Node class to store the elements of the Singly Linked List

    def __init__(self, e, n):
        self.element = e
        self.next = n
        # stores the element and the address to the next node (or None if it is the ending)
 
    def getElement(self):
        # function to return the element
        return self.element

    def getNext(self):
        # gets the next element
        return self.next
    
    def setNext(self, iNode):
        # sets a node as the next node
        self.next = iNode


class SLLIterator:
    # making an iterator for the singly liniked lists so that list traversal becomes very easy
    #we can use for-each to easily loop though the linked list
    def __init__(self, head):
        # we pass the head of a SinglyLinkedList to the SLLIterator class
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        # we define the process of the iteration here
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
        # I've made the tail node just in case.. As I was not very clear on solution

    def __len__(self):
        return self._size
        # we can just type len(the singly linked list object) and get its size

    def __iter__(self):
        # the iterator here redirects to the SLLIterator class
        return SLLIterator(self.head)

    def isEmpty(self):
        # a function to check if the list is empty or not
        return self._size == 0

    def addFirst(self, elem_val):
        # this can be used to add the element at the beginning of the linkedlist
        # also a point to note is that I haven't declared the head to contain a None element, rather I've set the first element as the head
        self.head = Node(elem_val, self.head)
        if self._size == 0:
            self.tail = self.head
        # although we initially defined tail to be the next node of head, here we are just making it to be the last element of the linked list, which continues in all the functions that add the elements...
        self._size+=1
    
    def addLast(self, elem_val):
        # this function adds the element at the end of the array
        iNode = Node(elem_val, None)
        if (self.isEmpty()):
            self.head = iNode
        else:
            self.tail.setNext(iNode)
        self.tail = iNode
        self._size += 1

    def add(self, elem_val):
        # this alson adds the function at the end... I just made it to keep the function name shorter
        self.addLast(elem_val)

    def __contains__(self, item):
    	# we defined this so that the `in` keyword can give a proper true or false
    	# supposing the linked list has the elements, say sl = [1,"hello",3]
    	# if we run `1 in sl` we get `True` and `"hello" not in sl` gives `False`
    	# so does `2 in sl`
        for node in self:
            if item == node.getElement():
                return True
        return False


    def pop(self):
        # I was unable to think of a better way than this to pop the last elelement for a singly linked list, so... I just went with it...
        # although it loops through the list everytime to pop the last element, it rather made the logic for the task pretty easy
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
