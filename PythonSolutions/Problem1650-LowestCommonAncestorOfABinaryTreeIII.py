# Definition for a Node.
import math
import sys
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, parent=None):
        self.val = val
        self.parent = parent

class Solution:

    def lowestCommonAncestor(self, p: TreeNode, q: TreeNode) -> TreeNode:
        a, b = p, q

        while a != b:
            if a is not None:
                a = a.parent
            else:
                a = q

            if b is not None:
                b = b.parent
            else:
                b = p

        return a

if __name__ == '__main__':
    testCases = {
        # 1: [TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), 5, 4],
        # 2: [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        # 3: [TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))]
    }

    # for key in testCases:
    root = TreeNode(3)
    node5 = TreeNode(5, parent=root)
    node1 = TreeNode(1, parent=root)
    node6 = TreeNode(6, parent=node5)
    node2 = TreeNode(2, parent=node5)
    node0 = TreeNode(0, parent=node1)
    node8 = TreeNode(8, parent=node1)
    node7 = TreeNode(7, parent=node2)
    node4 = TreeNode(4, parent=node2)

    print(f"{Solution().lowestCommonAncestor(node7, node8)}")