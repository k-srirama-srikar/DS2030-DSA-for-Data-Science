from singlylinkedlist import Node, SinglyLinkedList
x = input().split()

sl = SinglyLinkedList()

for i in x:
    sl.add(i)

def rearrange(sl_obj):
    new_sl = SinglyLinkedList()
    check_n = len(sl_obj)//2
    if len(sl_obj) == 2*check_n:
        check_n-=1
    # check_n is initialised to make sure that the elements are not repeated twice
    for node in sl_obj:       
        n1 = node.getElement()
        new_sl.add(n1)
        node2 = sl_obj.pop()
        n2 = node2.getElement()
        if check_n >0:
            new_sl.add(n2)
            check_n -= 1  
    return new_sl

sl = rearrange(sl)

for e in sl:
    print(e.getElement(), end=" ")
    if e.next!=None:
        print("->", end=" ")

