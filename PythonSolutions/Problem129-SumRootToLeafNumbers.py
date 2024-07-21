# Definition for a Node.
import math
import sys
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root: TreeNode, currentSum: int) -> int:
            if not root:
                return 0

            currentSum = currentSum * 10 + root.val

            if not root.left and not root.right:
                return currentSum
            else:
                return self.sumNumbers(root.left, currentSum) + self.sumNumbers(root.right, currentSum)

        return dfs(root, 0)

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(1, TreeNode(2), TreeNode(3))],
        2: [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        3: [TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))]
    }

    for key in testCases:
        print(f"{Solution().maxPathSum(testCases[key][0])}")
        print("\n------------------------------------------------------------------------\n")