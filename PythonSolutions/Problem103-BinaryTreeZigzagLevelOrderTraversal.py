# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        def addToQueue(root: Optional[TreeNode], level: int):
            nonlocal queue

            if not root:
                return

            if len(queue) < level + 1:
                queue.append([])

            # queue[level].append(root.val)
            if level % 2 == 1:
                queue[level].append(root.val)
                addToQueue(root.left, level + 1)
                addToQueue(root.right, level + 1)
            else:
                queue[level].insert(0, root.val)
                addToQueue(root.right, level + 1)
                addToQueue(root.left, level + 1)

            # addToQueue(root.left, level + 1)
            # addToQueue(root.right, level + 1)

        addToQueue(root, 0)
        return queue


if __name__ == '__main__':
    testCases = {
        1: [TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        2: [TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))],
        3: [TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(3, None, TreeNode(5)))],
    }

    for key in testCases:
        print(Solution().zigzagLevelOrder(testCases[key][0]))