# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root = TreeNode(postorder[-1])

        n = inorder.index(postorder[-1])

        left_subtree_inorder = inorder[:n]
        right_subtree_inorder = inorder[n+1:]

        left_subtree_postorder = postorder[:n]
        right_subtree_postorder = postorder[n:-1]

        root.left = self.buildTree(left_subtree_inorder, left_subtree_postorder)
        root.right = self.buildTree(right_subtree_inorder, right_subtree_postorder)

        return root

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)

if __name__ == '__main__':
    testCases = {
        1: [[9,3,15,20,7], [9,15,7,20,3]],
        2: [[-1], [-1]],
    }

    for key in testCases:
        print(f"{printTree(Solution().buildTree(testCases[key][0], testCases[key][1]))}")