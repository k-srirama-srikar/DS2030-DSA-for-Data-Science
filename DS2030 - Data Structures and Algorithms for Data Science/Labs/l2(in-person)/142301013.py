'''
K Srirama Srikar - 142301013
'''

import random

# Define the Contestant class
class Contestant:
    def __init__(self, name, chest_number, country, time=0):
        """
        Initialize the contestant with the following attributes:
        - name: The contestant's name.
        - chest_number: The contestant's chest number.
        - country: The country the contestant represents.
        - time: The time taken by the contestant in the heat (default is 0).
        """
        # TO DO
        self.name = name
        self.chest_number = chest_number
        self.country = country
        self.time = time
        # initialising the attirbutes of the Contestant class
        

    def __str__(self):
        """
        Return a formatted string representing the contestant.
        """
        # TO DO
        return f"{self.name} form {self.country}"
        # returns the formatted string whenever called

# Define the Node class for the doubly linked list
class Node:
    def __init__(self, contestant, prev=None, next=None):
        """
        Initialize the node with a contestant object.
        - contestant: The contestant object to store in this node.
        - prev: A reference to the previous node (initialized to None).
        - next: A reference to the next node (initialized to None).
        """
        # TO DO
        self.contestant = contestant
        self.prev = prev
        self.next = next
        # initialising the attributes for the doubly linked list class


# Define the LinkedList class for the doubly linked list
class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        - head: Points to the first node in the list.
        - tail: Points to the last node in the list.
        """
        self.head = None
        self.tail = None
        self._size = 0
        # making head, tail attributes and a non-public attribute size

    def __len__(self):
        # returns the size of the linked list
        return self._size

    def append(self, contestant):
        """
        Add a new contestant to the end of the list.
        - contestant: The contestant object to add to the list.
        - If the list is empty, set the head and tail to the new node.
        - Otherwise, add the new node to the end of the list.
        """
        # TO DO
        if self._size == 0:
            # adding to the end of the linkedlist
            self.head = Node(contestant)
            self.tail = self.head
            self._size += 1
        else:
            inode = Node(contestant, prev=self.tail)
            self.tail.next = inode
            self.tail = inode
            self._size += 1

        # adds the element at the end at the end of the linkedlist

    def sort_by_time(self):
        """
        Sort the list based on the time attribute of the contestants.
        - If the list is empty do nothing.
        - Otherwise perform insertion sort on the list
        """
        # TO DO
        if self._size == 0:
            return None

        dummy = Node(self.head.contestant, next=self.head)
        pre, curr = dummy, dummy.next
        
        while curr:
            # t = curr.next
            # print(curr.contestant)
            if pre.contestant.time <= curr.contestant.time:
                pre, curr = curr, curr.next
            p = dummy
            if curr != None:
                # break
                while p.contestant.time <= curr.contestant.time:
                    if p.next == None:
                        break
                    p = p.next
                
                temp = curr.next
                curr.next = p.next
                p.next = curr
                pre.next = temp
                curr = temp

        self.head = dummy.next



    def get_top_performers(self, M):
        """
        Retrieve the top M performers from the list.
        - M: The number of top performers to retrieve. The function returns a Python list of top performers.
        """
        # TO DO
        db = self.head
        l1 = []
            
        while True:
            l1.append(db.contestant)
            if db.next != None:
                db = db.next
            else:
                break

        l1.reverse()
        return l1[:M]


# Function to simulate heats recursively
def simulate_heats(contestants, N, M):
    """
    Simulate heats by dividing contestants into multiple heats, assigning random times,
    and recursively selecting the top performers until only one heat remains.
    - contestants: Python List of Contestant objects.
    - N: Number of contestants per heat.
    - M: Number of top performers to select from each heat.
    - Identify the base case - when the number of contestants is <= N.
    - Each heat is stored as a linked list.
    """
    # base case
    # number of contestants is <= N
    # - create a linkedlist of the contestants in the final heat
    # - sort the linkedlist by time
    # - select the top 3 performers and return them as a Python List
    # TO DO
    if len(contestants)<=N:
        l1 = LinkedList()
        for c in contestants:
            # print(c)
            c.time = random.randint(5,15)
            l1.append(c)
        l1.sort_by_time()
        finalists = l1.get_top_performers(3)
        # print(finalists)
        return finalists
    # the base case which gives the finalists


    # Divide contestants into heats in some random manner.
    # TO DO
    k = len(contestants)//N 
    m = len(contestants)%N
    # just to check if the elements are perfectly divisible
    heats = []
    con_copy = contestants[::]
    for i in range(k):
        heat = []
        for j in range(N): 
            con = random.choice(con_copy)
            con_copy.remove(con)
            heat.append(con)
            # adding random contestants to the heat
        print("Heat",heat)
        heats.append(heat)
    if m !=0:
        heats.append(con_copy)
    print("All", heats)

    # initialize a Python list that will store the contestants for the next round.
    next_round_contestants = []
    
    


    # Loop through each heat while
    # - assigning random times to each contestant in the heat
    # - create a linkedlist of the contestants in the heat
    # - sort the linkedlist by time
    # - select the top M performers from each heat
    # - append the top M performers to the list containing next round contestants.
    # TO DO
    for heat in heats:
        l1 = LinkedList()        
        for c in heat:
            c.time = random.randint(5,15)
            l1.append(c)
        l1.sort_by_time()
        # assigns randomly times to the contestants
        # and adds to the linked list
        next_round_contestants += l1.get_top_performers(M)


    
    # Call the simulate heats function on the set of contestants participating in the next level of heats.
    
    # TO DO
    return simulate_heats(next_round_contestants, N, M)


# Test cases
def test():
    contestants = [
        Contestant("Contestant A", 1, "Country A"),
        Contestant("Contestant B", 2, "Country B"),
        Contestant("Contestant C", 3, "Country C"),
        Contestant("Contestant D", 4, "Country D"),
        Contestant("Contestant E", 5, "Country E"),
        Contestant("Contestant F", 6, "Country F"),
        Contestant("Contestant G", 7, "Country G"),
        Contestant("Contestant H", 8, "Country H")
    ]
    
    N = 4  # Number of contestants per heat
    M = 2  # Number of top performers to select from each heat

    winners = simulate_heats(contestants, N, M)
    print("Final Selection:")
    medals = ["Gold", "Silver", "Bronze"]
    for i, winner in enumerate(winners):
       print(f"{medals[i]}: {winner}")

# Run the test case
test()
