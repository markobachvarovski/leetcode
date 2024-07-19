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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def solve(root, lvl):
            if not root:
                return

            if len(res) == lvl:
                res.append(root.val)

            solve(root.right, lvl + 1)
            solve(root.left, lvl + 1)

        res = []
        solve(root, 0)
        return res


if __name__ == '__main__':
    testCases = {
        1: [1,2,3,None,5,None,4],
        2: [1,None,3],
        3: [],
        4: [1, 2]
    }

    for key in testCases:
        print(f"{Solution().rightSideView(to_binary_tree(testCases[key]))}")