class TreeNode:
    def __init__(self, node_number, parent, left, right):
        self.node_number = node_number
        self.parent = parent
        self.left = left
        self.right = right


def build_tree_from_file(filename):
    nodes = {}
    with open(filename, 'r') as file:
        for line in file:
            node_number, parent, left, right = map(int, line.split())
            nodes[node_number] = TreeNode(node_number, parent, left, right)

        # Link child nodes
    for node in nodes.values():
        if node.left and node.left in nodes:
            node.left = nodes[node.left]
        else:
            node.left = None
        if node.right and node.right in nodes:
            node.right = nodes[node.right]
        else:
            node.right = None

    return nodes[1] if 1 in nodes else None


def are_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.node_number == root2.node_number and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))


def pre_order_traversal(node):
    if node is None:
        return
    else:
        # first print the parent ,then left child ,then right child
        print(node.nodenumber, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is None:
        return
    else:
        # first print the left child ,then right child,then parent
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.nodenumber, end=" ")


def are_isomorphic(root1, root2):
    """
    Check if two binary trees are identical.

    :param root1: TreeNode - Root of the first binary tree.
    :param root2: TreeNode - Root of the second binary tree.
    :return: bool - True if the trees are identical, False otherwise.
    """
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False

    without_swap = (are_isomorphic(root1.left, root2.left) and
                    are_isomorphic(root1.right, root2.right))
    with_swap = (are_isomorphic(root1.left, root2.right) and
                 are_isomorphic(root1.right, root2.left))
    if without_swap or with_swap:
        return count_isomorphic_ways(root1, root2)
    else:
        return 0


def count_isomorphic_ways(root1, root2):
    """
    Count the number of valid ways to transform T1 into T2 using swaps.

    :param root1: TreeNode - Root of the first binary tree (T1).
    :param root2: TreeNode - Root of the second binary tree (T2).
    :return: int - The number of valid ways to transform T1 into T2 by swapping nodes.
    """
    if not root1 and not root2:
        return 1
    if not root1 or not root2:
        return 0

    # If the node values of root1 and root2 differ, there is no valid way
    if root1.node_number != root2.node_number:
        return 0

    without_swap = count_isomorphic_ways(root1.left, root2.left) * count_isomorphic_ways(root1.right, root2.right)

    with_swap = count_isomorphic_ways(root1.left, root2.right) * count_isomorphic_ways(root1.right, root2.left)

    return without_swap + with_swap
    # return with_swap


def main():
    # Load trees from input files
    tree1_root = build_tree_from_file('tree1.txt')
    tree2_root = build_tree_from_file('tree2.txt')

    # Check if trees are identical
    if are_identical(tree1_root, tree2_root):
        print("The trees are identical.")
    else:
        print("The trees are not identical.")

    # Check if trees are isomorphic and count the number of transformations
    if are_isomorphic(tree1_root, tree2_root):
        ways = count_isomorphic_ways(tree1_root, tree2_root)
        print(f"The trees are isomorphic. Number of transformations: {ways}")
    else:
        print("The trees are not isomorphic.")


if __name__ == "__main__":
    main()
