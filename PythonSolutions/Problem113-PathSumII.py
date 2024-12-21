from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, remaining, path):
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val

            if node.left is None and node.right is None and remaining == 0:
                paths.append(path[:])
            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            path.pop()
            remaining += node.val

        paths = []
        dfs(root, targetSum, [])
        return paths

if __name__ == '__main__':
    testCases = {
        1: [TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)), None), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22],
    }

    for key in testCases:
        print(f"{Solution().pathSum(testCases[key][0], testCases[key][1])}")