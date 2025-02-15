from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = [0] * n  # 0: unvisited, 1: visiting, 2: safe

        def dfs(node):
            if visited[node] > 0:
                return visited[node] == 2

            visited[node] = 1
            for neighbor in graph[node]:
                if visited[neighbor] == 1 or not dfs(neighbor):
                    return False

            visited[node] = 2
            return True

        for i in range(n):
            if dfs(i):
                safe[i] = True

        return [i for i in range(n) if safe[i]]


if __name__ == '__main__':
    testCases = {
        1: [[1,2],[2,3],[5],[0],[5],[],[]],
        2: [[1,2,3,4],[1,2],[3,4],[0,4],[]],
        3: [[0],[2,3,4],[3,4],[0,4],[]]
    }

    for key in testCases:
        print(Solution().eventualSafeNodes(testCases[key]))