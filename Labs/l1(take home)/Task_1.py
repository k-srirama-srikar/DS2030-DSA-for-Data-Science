from singlylinkedlist import Node, SinglyLinkedList
x = input().split()
# storing the input vbalues in a list initially
sl = SinglyLinkedList()

for i in x:
    sl.add(i)

# adding the elements of the list to the singly linked list object

def rearrange(sl_obj):
    # the function to rearrange the elements of the linked list
    new_sl = SinglyLinkedList()
    # an empty list to which we append everything
    check_n = len(sl_obj)//2
    if len(sl_obj) == 2*check_n:
        check_n-=1
    # check_n is initialised to make sure that the elements are not repeated twice
    for node in sl_obj:       
        n1 = node.getElement()
        new_sl.add(n1)
        # we add the current element and the last element and remove the last element to make the list shorter
        node2 = sl_obj.pop()
        n2 = node2.getElement()
        if check_n >0:
            new_sl.add(n2)
            check_n -= 1  
            # just to make sure that the last element is nott added
    return new_sl

sl = rearrange(sl)

for e in sl:
    print(e.getElement(), end=" ")
    if e.next!=None:
        print("->", end=" ")
