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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")  # placeholder to be updated
        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable

            if node is None:
                return 0
            gain_on_left = max(get_max_gain(node.left), 0)  # Read the part important observations
            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations

            current_max_path = node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
            max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

            return node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path


if __name__ == '__main__':
    testCases = {
        1: [TreeNode(1, TreeNode(2), TreeNode(3))],
        2: [TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))],
        3: [TreeNode(1, TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)), TreeNode(-3, TreeNode(-2)))]
    }

    for key in testCases:
        key = 3
        print(f"{Solution().maxPathSum(testCases[key][0])}")
        print("\n------------------------------------------------------------------------\n")