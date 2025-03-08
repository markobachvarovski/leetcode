from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            nonlocal ans
            if not node:
                return
            if not node.left and not node.right:
                ans.append(node.val)

            dfs(node.left)
            dfs(node.right)

        if not root:
            return []
        ans = [root.val]

        node = root.left
        while node:
            if node.left or node.right:
                ans.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        dfs(root.left)
        dfs(root.right)

        node = root.right
        temp_ans = []
        while node:
            if node.left or node.right:
                temp_ans.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        ans.extend(temp_ans[::-1])

        return ans

if __name__ == '__main__':
    testCases = {
        1: TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10)), None))
    }

    for key in testCases:
        print(Solution().boundaryOfBinaryTree(testCases[key]))

