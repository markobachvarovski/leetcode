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

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root

        return l or r

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), 5, 4],
        # 2: [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        # 3: [TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))]
    }

    for key in testCases:
        print(f"{Solution().lowestCommonAncestor(testCases[key][0], testCases[key][1], testCases[key][2])}")