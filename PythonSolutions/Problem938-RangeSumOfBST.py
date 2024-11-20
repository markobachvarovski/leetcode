from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


if __name__ == '__main__':
    testCases = {
        1: [TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15]
    }

    for key in testCases:
        print(Solution().rangeSumBST(testCases[key][0], testCases[key][1], testCases[key][2]))
