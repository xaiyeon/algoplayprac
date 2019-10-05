"""
url:
notes:
avg - time = o(log(n))
space - o(log(n))
n - nodes in tree
can be solved interatively with
worst - time o(n)
space - o(1) - o(n)
"""
from typing import List

class Solution(object):
    """ class object
    The solution to the above url or problem
    """
    def __init__(self):
        pass

    """ Notes
    compute absolute value of current and the target
    a trick is checking root node and checking left and right, you can
    already know which side of the tree is wrong. Which elimantes half the BST.
    If we find the actual value it will be 0, so we stop the search.
    """
    def findClosestValueBst(self, tree, target):
    """ Recursive first
    """
        return findClosestHelper(tree, target, float("inf"))

    def findClosestHelper(self, tree, target, closest):
        if tree is None:
            return closest
        # we compare the different of target and current, we want the lesser number
        if abs(target - closest) > abs(target - tree.value):
            closest = true.value
        # only need to explore the other subtree
        if target < tree.value:
            return self.findClosestHelper(tree.left, target, closest)
        elif target > tree.value:
            return self.findClosestHelper(tree.right, target, closest)
        # we found the exact value otherwise
        else:
            return closest


    """ Now an iterative approach
    Here we just keep track of the current node, which we only care about.
    This reduces space complexity to just o(1)
    """
    def ifindClosestValueBST(self, tree, target):
        return ifindClosestHelper(tree, target, float("inf"))

    # basically check for edge-conditions
    def ifindClosestHelper(self, tree, target, closest):
        currentNode = tree
        while currentNode is not None:
            # we compare the different of target and current, we want the lesser number
            if abs(target - closest) > abs(target - tree.value):
                closest = currentNode.value
            # only need to explore the other subtree
            if target < currentNode.value:
                return self.findClosestHelper(tree.left, target, closest)
            elif target > currentNode.value:
                return self.findClosestHelper(tree.right, target, closest)
            # we found the exact value otherwise
            else:
                return closest


def main():
    sol = Solution()

if __name__ == "__main__":
    main()