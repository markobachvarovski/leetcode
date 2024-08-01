from collections import deque
from typing import Optional, List, Set


class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()
        def addCell(r, c, timeElapsed):
            if (
                r < 0
                or c < 0
                or r == rows
                or c == cols
                or (r, c) in visited
            ):
                return
            visited.add((r, c))
            q.append([r, c, timeElapsed])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r, c))
                if grid[r][c] == 2:
                    q.append([r, c, 0])
                    visited.add((r, c))

        timeElapsed = 0
        while q:
            for i in range(len(q)):
                r, c, timeElapsed = q.popleft()
                addCell(r + 1, c, timeElapsed + 1)
                addCell(r - 1, c, timeElapsed + 1)
                addCell(r, c + 1, timeElapsed + 1)
                addCell(r, c - 1, timeElapsed + 1)

        if len(visited) != rows * cols:
            return -1
        return timeElapsed


if __name__ == '__main__':
    testCases = {
        1: [
            [2,1,1],
            [1,1,0],
            [0,1,1]
        ],
        2: [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ],
        3: [[0,2]]
    }

    for key in testCases:
        print(Solution().orangesRotting(testCases[key]))