# Definition for a Node.
import math
import sys
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = []

        def addToQueue(root: Optional[TreeNode]):
            if not root:
                return

            addToQueue(root.left)
            self.queue.append(root)
            addToQueue(root.right)

        self.pointer = 0
        self.queue.append(TreeNode(float('-inf')))
        addToQueue(root)

    def next(self) -> int:
        self.pointer += 1
        return self.queue[self.pointer].val

    def hasNext(self) -> bool:
        return self.pointer + 1 != len(self.queue)

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))],
        # 2: [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        # 3: [TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))]
    }

    for key in testCases:
        bst = BSTIterator(testCases[key][0])
        for x in bst.queue:
            print(x.val)