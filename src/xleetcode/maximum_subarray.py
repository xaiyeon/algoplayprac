"""
url: https://leetcode.com/problems/maximum-subarray/
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

    def maxSubArray(self, nums: List[int]) -> int:
        for n in nums:
            print(n)

def main():
    sol = Solution()
    input = [-2,1,-3,4,-1,2,1,-5,4]
    sol.maxSubArray(input)


if __name__ == "__main__":
    main()