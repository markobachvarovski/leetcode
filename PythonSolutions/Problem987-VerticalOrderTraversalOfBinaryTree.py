# Definition for a Node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        horizontalDistance = defaultdict(list)
        answer = []
        def dfs(node, distance, height):
            if not node:
                return

            horizontalDistance[distance].append((node.val, height))
            dfs(node.left, distance - 1, height + 1)
            dfs(node.right, distance + 1, height + 1)

        dfs(root, 0, 0)

        for key in sorted(horizontalDistance.keys()):
            horizontalDistance[key].sort(key=lambda x: (x[1], x[0]))
            answer.append([val for val, _ in horizontalDistance[key]])

        return answer

if __name__ == '__main__':
    testCases = {
        1: TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        2: TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    }

    for key in testCases:
        print(Solution().verticalTraversal(testCases[key]))