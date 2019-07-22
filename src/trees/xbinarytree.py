"""
    Practicing binary trees

    Pre-order Traversal:
    1. Check if current node is empty/null
    2. Display data part of root or curr node
    3. Traverse left subtree recursively call pre-order function
    4. Traverse right subtree recursively call pre-order function

"""

class xNode(object):
    """ class object
    A data inside xBinaryTree
    """
    def __init__(self, value, name=None):
        self.value = value
        self.left = None
        self.right = None
        # cross is used for new experiment
        self.cross = None

class xBinaryTree(object):
    """ class object
    Holds objects of xNode
    Functions related to binary tree operations
    """
    def __init__(self, root):
        self.root = xNode(root)

    def print_tree(self, traversal_type):
        """ printing the tree
        traversal_type: string
        """
        if traversal_type == "preorder":
            return self.xpreorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.xinorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.xpostorder_print(self.root, "")
        else:
            print("Traversal type {} is not supported".format(traversal_type))
            return False

    """
        Below are recursive solutions
    """
    def xpreorder_print(self, start, traversal):
        """ 
        Root -> Left -> Right
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.xpreorder_print(start.left, traversal)
            traversal = self.xpreorder_print(start.right, traversal)
        return traversal

    def xinorder_print(self, start, traversal):
        """
        Left -> Root -> Right
        """
        if start:
            traversal = self.xinorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.xinorder_print(start.right, traversal)
        return traversal

    def xpostorder_print(self, start, traversal):
        """
        Left -> Right -> Root
        """
        if start:
            traversal = self.xpostorder_print(start.left, traversal)
            traversal = self.xpostorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal            

    """
        End of recursive solutions
    """

""" What tree looks like
        1
    4       10
   6 8     13 21
"""
def main():
    print("xBinaryTree Practice")
    # Making a binary tree
    xTree = xBinaryTree(1)
    xTree.root.left = xNode(4)
    xTree.root.right = xNode(10)
    xTree.root.left.left = xNode(6)
    xTree.root.left.right = xNode(8)
    xTree.root.right.left = xNode(13)
    xTree.root.right.right = xNode(21)
    print(xTree.print_tree("preorder"))
    print(xTree.print_tree("inorder"))
    print(xTree.print_tree("postorder"))


if __name__ == "__main__":
    main()