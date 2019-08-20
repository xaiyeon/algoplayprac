"""
url: https://www.algoexpert.io/questions/Find%20Three%20Largest%20Numbers
notes:
easy one :D
"""
from typing import List

class Solution(object):
    """ class object
    A data inside xBinaryTree
    """
    def __init__(self, name=None):
        self.name = name

    # remember variables used in multiple functions are within the same scope!
    def findThreeLargestNumbers(self, nums: List[int]) -> int:
        """ main solution function
        """
        # the trick here was to break it up into helper functions :D
        threelarge = [None, None, None]
        testScope = 0
        for n in nums:
            # for the first three of course we will keep it
            self.checkBigThree(threelarge, n, testScope)
        print(threelarge)
        print(testScope)
    
    # expression are evaluated from left first to right!
    def checkBigThree(self, threelarge, n, testScope):
        testScope = 5
        if threelarge[2] is None or threelarge[2] < n:
            self.updateThreeLarge(threelarge, n, 2)
        
        elif threelarge[1] is None or threelarge[1] < n:
            self.updateThreeLarge(threelarge, n, 1)
        
        elif threelarge[0] is None or threelarge[0] < n:
            self.updateThreeLarge(threelarge, n, 0)
        
    def updateThreeLarge(self, threelarge, num, index):
        for i in range(index + 1):
            if i == index:
                threelarge[i] = num
            else:
                threelarge[i] = threelarge[i + 1]

def main():
    sol = Solution()
    input = [12,0,-2,-4,24,500,-23,234,0,1,5,5,567]
    sol.findThreeLargestNumbers(input)


if __name__ == "__main__":
    main()