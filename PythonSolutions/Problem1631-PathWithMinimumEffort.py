from collections import deque, defaultdict
from typing import Optional, List, Set
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        min_heap = [(0, (0, 0))]  # (effort, (i, j))
        weights = [[float("inf")] * cols for _ in range(rows)]
        weights[0][0] = 0

        while len(min_heap) > 0:
            effort, coords = heapq.heappop(min_heap)

            if coords == (len(heights) - 1, len(heights[-1]) - 1):
                return effort

            if coords in visited:
                continue
            visited.add(coords)

            i, j = coords

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < rows and 0 <= y < cols:
                    new_effort = max(effort, abs(heights[i][j] - heights[x][y]))

                    if new_effort < weights[x][y]:
                        weights[x][y] = new_effort
                        heapq.heappush(min_heap, (new_effort, (x, y)))

        return -1


if __name__ == '__main__':
    testCases = {
        1: [[1,2,2],[3,8,2],[5,3,5]],
        2: [[1,2,3],[3,8,4],[5,3,5]],
        3: [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]],
        4: [[1,10,6,7,9,10,4,9]]
    }

    for key in testCases:
        print(Solution().minimumEffortPath(testCases[key]))