# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> TreeNode:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right


    # Recursive and iterative approach
    def flattenRoot(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        currRight = root.right
        root.right = self.flattenRoot(root.left)

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = self.flattenRoot(currRight)
        root.left = None

        return root

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
        1: [TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))],
        2: [TreeNode(1, None, TreeNode(2, TreeNode(3), None))]
    }

    for key in testCases:
        # key = 2
        print(f"{print2D(Solution().flatten(testCases[key][0]))}")
        print("\n------------------------------------------------------------------------\n")