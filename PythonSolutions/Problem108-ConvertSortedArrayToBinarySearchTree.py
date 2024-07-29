# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        i = len(nums) // 2
        node = TreeNode(nums[i])

        node.left = self.sortedArrayToBST(nums[:i])
        node.right = self.sortedArrayToBST(nums[i + 1:])

        return node

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
        1: [-10,-3,0,5,9],
    }

    for key in testCases:
        print(f"{print2D(Solution().sortedArrayToBST(testCases[key]))}")
        print("\n------------------------------------------------------------------------\n")