from typing import List
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def add_node_to_graph(root):
            if not root:
                return

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                add_node_to_graph(root.left)

            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                add_node_to_graph(root.right)

        if not root:
            return []
        add_node_to_graph(root)

        ans = []
        q = deque()
        q.append([target.val, 0])
        visited = set()

        while len(q) > 0:
            num, distance = q.popleft()
            if num in visited:
                continue
            visited.add(num)

            if distance == k:
                ans.append(num)
                continue

            for neighbour in graph[num]:
                q.append([neighbour, distance + 1])

        return ans


if __name__ == '__main__':
    testCases = {
        1: [TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8))), TreeNode(5), 2],
        2: [TreeNode(1), TreeNode(1), 3]
    }

    for key in testCases:
        print(Solution().distanceK(testCases[key][0], testCases[key][1], testCases[key][2]))