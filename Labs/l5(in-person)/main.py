# Define the structure of the binary tree node
class TreeNode :
    def __init__ (self, val) :
        self.val = val
        self.left = None
        self.right = None
    # Binary Search Tree Class
class BinarySearchTree :
    def __init__ (self) :
        self.root = None

    # a helper insert method to insert an element
    @staticmethod
    def _recursive_insert(node, val):
        if val<node.val:
            if node.left==None:
                # if the left element is none, it implies that, that is where the element needs to be inserted
                node.left=TreeNode(val)
                return
            # else we call the function recursively, passing the left node
            BinarySearchTree._recursive_insert(node.left, val)
        elif val>node.val:
            if node.right==None:
                # if the right element is none, it implies that, that is where the element needs to be inserted
                node.right=TreeNode(val)
                return
            # else we call the function recursively, passing the right node
            BinarySearchTree._recursive_insert(node.right, val)


    # helper function for search
    @staticmethod
    def _recursive_search(node, val):
        if node==None:
            # case where the element is not in the Binary Search Tree
            return False
        if node.val==val:
            # case where we find the value
            return True
        elif val<node.val:
            # else we search for the left subtree if it is less than the value at the current node
            return BinarySearchTree._recursive_search(node.left, val)
        elif val>node.val:
            # else we search for the right subtree if it is more than the value at the current node
            return BinarySearchTree._recursive_search(node.right, val)

    # TODO : Implement this function
    def insert (self, val) :
        if self.root==None:
            # inserts the element at the root
            self.root = TreeNode(val)
        else:
            # adds thye element at other positions by calling the helper function
            BinarySearchTree._recursive_insert(self.root, val)

    # TODO : Implement this function
    def search (self, val) :
        if self.root is not None:
            # just to ensure if we are not serching in an empty tree 
            if self.root.val == val:
                # checks if it is at the root
                return True
        # calling the helper function
        return BinarySearchTree._recursive_search(self.root, val)

    # helper function for inorder traversal
    @staticmethod
    def _print_inorder(node,l):
        if not node:
            # if its empty we return
            return
        # first the left child
        BinarySearchTree._print_inorder(node.left, l)
        # then the node
        l.append(node.val)
        # lastly, the right child
        BinarySearchTree._print_inorder(node.right, l)

    # TODO : Implement this function
    def inorder_traversal(self):
        curr = self.root
        l=[]
        # where we append the elements in the inorder traversal format
        BinarySearchTree._print_inorder(curr, l)
        return l
    
    # we generate all the possible combinations of a1 and a2 whilst maintsining the order
    @staticmethod
    def _array_mutate(a1,a2,i1=0,i2=0,a3=[],final=[]):
        if i1==len(a1):
            # if we travese through one list we just add the remaining elements of the other list
            a3+=a2[i2:]
            final.append(a3)
            return
        elif i2==len(a2):
            a3+=a1[i1:]
            final.append(a3)
            return
        BinarySearchTree._array_mutate(a1,a2,i1+1,i2,a3+[a1[i1]], final)
        # adding all the possible combinations by adding an element either from a1 or a2
        BinarySearchTree._array_mutate(a1,a2,i1,i2+1,a3+[a2[i2]], final)
        return final


    @staticmethod
    def _recursive_permutations(node):
        if node.left and node.right:
            if node.left.left is None and node.left.right is None and node.right.left is None and node.right.right is None:
                # this is the case where a node just has to leaf nodes as its children
                return [[node.val,node.left.val,node.right.val], [node.val, node.right.val, node.left.val]]
            lp = BinarySearchTree._recursive_permutations(node.left)
            rp = BinarySearchTree._recursive_permutations(node.right)
            combos = []
            # list that stores all the combinations
            for l in lp:
                for r in rp:
                    # adding each of the combinations to the list
                    combos+=(BinarySearchTree._array_mutate(l,r))
            combos = [[node.val]+x for x in combos]
            # adds the current element to all the combinations
            return combos
            
        if not node.left:
            # case where the left node is null
            if node.right:
                if node.right.left in None and node.right.right is None:
                    return [[node.val,node.right.val]]
                    # the case where the right node is the end
                else:
                    return [[node.val]+x for x in BinarySearchTree._recursive_permutations(node.right)]
                    # case where the node does not have a value at left child but theres a subtree at right child
            else:
                return [[node.val]]
                # if its a leaf node, it'll be mostly unused unoless the bst is inclined to one side
        else:
            if node.left.left is None and node.left.right is None:
                return [[node.val,node.left]]
            else:
                return [[node.val]+x for x in BinarySearchTree._recursive_permutations(node.left)]
                # case where the node does not have a value at right child but theres a subtree at left child
            
        
    def permutations(self):
        curr = self.root
        print(BinarySearchTree._recursive_permutations(curr))
        # the permutations function calls a helper function which computes all the possible orders



# Example usage
if __name__ == "__main__" :
    bst = BinarySearchTree()
    elements = [5 , 3 , 8 , 2 , 4 , 7 , 9]
    for elem in elements :
        bst.insert(elem)

# Call the inorder_traversal to see the tree ’s sorted values
print ( " Inorder Traversal : " , bst.inorder_traversal())
# Search for a value
search_value = 4
print (f" Is {search_value} in the tree ? {bst.search(search_value)}")
# the below statement prints out all the possible permutations of the elements list which yield the same tree
bst.permutations()
