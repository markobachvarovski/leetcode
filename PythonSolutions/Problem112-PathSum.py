# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum
        else:
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

COUNT = [10]
def print2DUtil(root, space):
    if root is None:
        return

    space += COUNT[0]

    print2DUtil(root.right, space)
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.val)

    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))), 22],
        # 2: [TreeNode(1, None, TreeNode(2, TreeNode(3), None))]
    }

    for key in testCases:
        # key = 2
        print(f"{Solution().hasPathSum(testCases[key][0], testCases[key][1])}")
        print("\n------------------------------------------------------------------------\n")