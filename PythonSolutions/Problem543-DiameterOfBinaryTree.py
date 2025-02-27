from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxLength = 0

        def getLength(node):
            nonlocal maxLength

            if not node:
                return 0

            leftLength = getLength(node.left)
            rightLength = getLength(node.right)

            maxLength = max(maxLength, leftLength + rightLength)

            return max(leftLength, rightLength) + 1

        getLength(root)
        return maxLength

if __name__ == '__main__':
    testCases = {
        1: TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        2: TreeNode(1, TreeNode(2))
    }

    for key in testCases:
        print(Solution().diameterOfBinaryTree(testCases[key]))

