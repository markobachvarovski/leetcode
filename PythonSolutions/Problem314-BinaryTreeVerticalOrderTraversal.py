from typing import List

from collections import defaultdict, deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        ans = []

        q = deque()
        if root:
            q.append((root, 0))

        while len(q) > 0:
            node, level = q.popleft()
            columns[level].append(node.val)

            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        for key in sorted(columns.keys()):
            ans.append(columns[key])

        return ans


if __name__ == '__main__':
    testCases = {
        1: TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
        2: None,
        3: TreeNode(1),
        4: TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
        5: TreeNode(1,
            TreeNode(2,
                TreeNode(4,
                    TreeNode(8,
                        TreeNode(12), None), None),
                TreeNode(5,
                    TreeNode(9,
                        TreeNode(13,
                            TreeNode(16), None), None),
                    TreeNode(10,
                        None, TreeNode(14,
                            None, TreeNode(17))))),
            TreeNode(3,
                TreeNode(6),
                TreeNode(7,
                    None,
                    TreeNode(11,
                        None,
                        TreeNode(15)))))
    }

    for key in testCases:
        print(Solution().verticalOrder(testCases[key]))
