from collections import deque, defaultdict
from typing import Optional, List, Set


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visited = set()

        for pair in edges:
            node1, node2 = pair
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        def dfs(node, prev):
            nonlocal visited
            if node in visited:
                return False

            visited.add(node)
            for adj in adj_list[node]:
                if adj == prev:
                    continue
                else:
                    if not dfs(adj, node):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n





if __name__ == '__main__':
    testCases = {
        1: [5, [[0, 1], [0, 2], [0, 3], [1, 4]]],
        2: [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]]
    }

    for key in testCases:
        print(Solution().validTree(testCases[key][0], testCases[key][1]))