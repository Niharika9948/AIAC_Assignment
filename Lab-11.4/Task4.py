class Node:
    """
    Node of a Binary Search Tree.

    Attributes:
        data (int): Value stored in the node.
        left (Node): Left child node.
        right (Node): Right child node.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree (BST) implementation.

    Methods:
        insert(value): Inserts a value into the BST.
        search(value): Searches for a value in the BST, returns True if found.
        inorder_traversal(): Returns a list of all values in the BST in ascending order.
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Args:
            value (int): The value to insert.
        """
        def _insert(node, value):
            if node is None:
                return Node(value)
            if value < node.data:
                node.left = _insert(node.left, value)
            elif value > node.data:
                node.right = _insert(node.right, value)
            # If value == node.data, do not insert duplicates (BST property)
            return node

        self.root = _insert(self.root, value)

    def search(self, value):
        """
        Search for a value in the BST.

        Args:
            value (int): The value to search for.

        Returns:
            bool: True if value exists, False otherwise.
        """
        def _search(node, value):
            if node is None:
                return False
            if value == node.data:
                return True
            elif value < node.data:
                return _search(node.left, value)
            else:
                return _search(node.right, value)
        return _search(self.root, value)

    def inorder_traversal(self):
        """
        Return all values in the BST in ascending order.

        Returns:
            List[int]: Inorder traversal as a sorted list of values.
        """
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)

        _inorder(self.root)
        return result

if __name__ == "__main__":
    # Test the BST with a list of integers
    bst = BST()
    values = [7, 3, 9, 1, 5, 8, 10]
    print("Inserting values:", values)
    for v in values:
        bst.insert(v)

    print("Inorder traversal:", bst.inorder_traversal())

    # Test search()
    test_search = [5, 11, 7, 0, 10]
    for target in test_search:
        found = bst.search(target)
        print(f"Search {target}: {'Found' if found else 'Not found'}")
