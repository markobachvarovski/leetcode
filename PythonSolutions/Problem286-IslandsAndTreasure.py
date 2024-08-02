from collections import deque
from typing import Optional, List, Set


class Solution:
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def addCell(r, c):
            if (
                min(r, c) < 0
                or r == rows
                or c == cols
                or (r, c) in visited
                or grid[r][c] == -1
            ):
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1



if __name__ == '__main__':
    testCases = {
        1: [
            [2147483647,         -1,          0, 2147483647],
            [2147483647, 2147483647, 2147483647,         -1],
            [2147483647,         -1, 2147483647,         -1],
            [         0,         -1, 2147483647, 2147483647]
        ],
    }

    for key in testCases:
        Solution().islandsAndTreasure(testCases[key])
        print(testCases[key])