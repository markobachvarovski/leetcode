# Definition for a Node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def to_binary_tree(items):
    if not items:
        return None

    it = iter(items)
    root = TreeNode(next(it))
    q = [root]
    for node in q:
        val = next(it, None)
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        val = next(it, None)
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
    return root

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])

        n = inorder.index(preorder[0])

        left_subtree_inorder = inorder[:n]
        right_subtree_inorder = inorder[n+1:]

        left_subtree_preorder = preorder[1:n+1]
        right_subtree_preorder = preorder[n+1:]

        root.left = self.buildTree(left_subtree_preorder, left_subtree_inorder)
        root.right = self.buildTree(right_subtree_preorder, right_subtree_inorder)

        return root

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)

if __name__ == '__main__':
    testCases = {
        1: [[3,9,20,15,7], [9,3,15,20,7]],
        2: [[-1], [-1]],
    }

    for key in testCases:
        print(f"{printTree(Solution().buildTree(testCases[key][0], testCases[key][1]))}")