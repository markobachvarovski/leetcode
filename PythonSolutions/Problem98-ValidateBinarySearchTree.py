from typing import Optional


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
class Solution(object):
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not (inorder(node.left) and prev < node.val):
                return False
            prev = node.val
            return inorder(node.right)

        return inorder(root)


if __name__ == '__main__':
    testCases = {
        1: [2,1,3],
        2: [5,1,4, None, None,3,6],
        3: [2,2,2],
        4: [5,4,6,None,None,3,7]
    }

    for key in testCases:
        print(f"{Solution().isValidBST(to_binary_tree(testCases[key]))}")