from singlylinkedlist import SinglyLinkedList

number = int(input())
bookmark_set = SinglyLinkedList()
# a singlylinkedlist to keep track of the results that we have gotten and if it is in it, that implies that the number is not happy
s1 = 0
sum1 = 0
def recurr_sum(n):
    # a recursive function to add the numbers in the number
    if n<10:
        return n**2
    else:
        s = recurr_sum(n//10) + (n%10)**2
        return s
s_init = recurr_sum(number)
# the initial sum
is_happy = True if s_init == 1 else False
bookmark_set.add(s_init)
# adding it to the bookmark set
sum1 = s_init
while sum1 !=1:
    sum1 = recurr_sum(sum1)
    # to check all the sums that come after the initial
    if sum1 == 1:
        is_happy = True
        break
    elif sum1 not in bookmark_set:
        bookmark_set.add(sum1)
    elif sum1 in bookmark_set:
        break

print(is_happy)

