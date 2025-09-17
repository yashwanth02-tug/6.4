class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        def _insert(node, data):
            if node is None:
                return Node(data)
            if data < node.data:
                node.left = _insert(node.left, data)
            elif data > node.data:
                node.right = _insert(node.right, data)
            # If data == node.data, do not insert duplicates
            return node
        self.root = _insert(self.root, data)
    def search(self, data):
        def _search(node, data):
            if node is None:
                return False
            if data == node.data:
                return True
            elif data < node.data:
                return _search(node.left, data)
            else:
                return _search(node.right, data)
        return _search(self.root, data)
    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)
        _inorder(self.root)
        return result
if __name__ == "__main__":
    # Test the BST implementation
    bst = BST()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for num in nums:
        bst.insert(num)
    print("Inorder traversal:", bst.inorder_traversal())  # Should be sorted
    # Test search for present elements
    for val in [30, 70, 60]:
        print(f"Search {val}: {bst.search(val)}")  # Should be True
    # Test search for absent elements
    for val in [10, 35, 90]:
        print(f"Search {val}: {bst.search(val)}")  # Should be False
