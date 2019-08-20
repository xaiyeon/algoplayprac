"""
url: https://www.algoexpert.io/questions/Depth-first%20Search
notes: learn DFS and BFS
"""
from typing import List

class Solution(object):
    """ class object
    The solution to the above url or problem
    """
    def __init__(self, name=None):
        self.name = name

class Node(Solution):
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for c in array:
            c.depthFirstSearch(array)
        return array
        
def main():
    sol = Solution()
    blank = []
    solNode = Node("A")
    solNode.addChild("B").addChild("C").addChild("D").addChild("F")
    solNode.children[0].addChild("H")
    solNode.children[0].addChild("J")
    solNode.children[1].addChild("K")
    solNode.children[2].addChild("L").addChild("N")
    solNode.children[2].children[1].addChild("O")
    solNode.depthFirstSearch(blank)

if __name__ == "__main__":
    main()