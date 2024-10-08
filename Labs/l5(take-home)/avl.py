class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New nodes are initially added at height 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root = None, key=None):
        # the normal BST insert
        if not root:
            if not self.root:
                # case where the root node is none
                self.root = Node(key)
                root = self.root
                return root
            # the base case where, if the node is None we add a Node
            root = Node(key)
            return root
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # update the height of this ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # get the balance factor
        balance = self.get_balance(root)

        # If the node becomes unbalanced, then there are 4 cases
        
        # Here Node is z (the first place where the imbalance occurs)

        # Left Left Case
        #       z
        #      / 
        #     y  
        #    /   
        #   x
        # balance > 1
        # key < Node.left.key
        # this implies,
        # right_rotation(Node)
        
        # Right Right Case
        #   z
        #    \   
        #     y
        #      \
        #       x
        # blance < -1
        # key > Node.right.key
        # this implies,
        # left_rotation(Node)
                
        # Left Right Case
        #       z
        #      / 
        #     y  
        #      \   
        #       x
        # balance > 1
        # key > Node.left.key
        # this implies,
        # left_rotation(Node.left)
        # right_rotation(Node)

        # Right Left Case
        #   z
        #    \   
        #     y
        #    /
        #   x
        # blance < -1
        # key > Node.right.key
        # right_rotation(Node.right)
        # left_rotation(Node)


        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotation(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotatation(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotatation(root.left)
            return self.right_rotation(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotation(root.right)
            return self.left_rotatation(root)

        return root

    def delete(self, root=None, key=None):
        # initially we perform the genaral binary search tree delete
        if not root:
            if not self.root:
                # the case where the root node is null
                print("Deletion in an empty tree")
                return None
            print("Element not present for deletion")
            return root

        if key < root.key:
            # if key is less then the the key of the current node we recursively traverse the left subtree
            root.left = self.delete(root.left, key)
        elif key > root.key:
            # if key is more than the key of the current node we recursively traverse the right subtree
            root.right = self.delete(root.right, key)
        else:
            # root the node that has to be deleted
            # case where node is with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # case of node with two children
            # we get the inorder successor (smallest in the right subtree)
            temp = self.get_inorder_successor(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        # If the tree had only one node then return
        if root is None:
            return root

        # after deleting we have to update the heights
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # and then check for the balance
        balance = self.get_balance(root)

        # cases where unbalance can occur

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotation(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotatation(root.left)
            return self.right_rotation(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotatation(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotation(root.right)
            return self.left_rotatation(root)

        return root

    def get_inorder_successor(self, node):
        if node is None or node.left is None:
            return node
        return self.get_inorder_successor(node.left)

    def left_rotatation(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def right_rotation(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, node):
        # made to check if the program is working properly
        if not node:
            return
        print(f"{node.key} ", end="")
        self.pre_order(node.left)
        self.pre_order(node.right)
    

if __name__ == "__main__":
    tree = AVLTree()
    
    print("Menu: \n1 -> Insert\n2 -> Delete\nq -> Quit\nEnter an option from the above options of the form \n1 {key} - to insert the key\n2 {key} - to delete the key\nq - to quit")

    is_true = True
    while is_true:
        l = input().split()
        if l[0] == '1':
            l = [int(x) for x in l]
            tree.root = tree.insert(root=tree.root,key=l[1])
        elif l[0] == '2':
            l = [int(x) for x in l]
            tree.root = tree.delete(root=tree.root,key=l[1])
        elif l[0]=='p':
            # for checking the functionality
            tree.pre_order(tree.root)
            print()
        else:
            is_true = False


