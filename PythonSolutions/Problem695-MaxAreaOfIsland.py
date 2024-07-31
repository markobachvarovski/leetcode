from collections import deque
from typing import Optional, List, Set


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxSize,currSize = 0, 0
        visited = set()
        def dfs(r, c):
            nonlocal currSize
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1 or (r,c) in visited:
                return

            currSize += 1
            visited.add((r,c))

            dfs(r + 1, c),
            dfs(r - 1, c),
            dfs(r, c + 1),
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    currSize = 0
                    dfs(r, c)
                    maxSize = max(maxSize,currSize)

        return maxSize



if __name__ == '__main__':
    testCases = {
        1: [
          [1,1,1,1,0],
          [1,1,0,1,0],
          [1,1,0,0,0],
          [0,0,0,0,0]
        ],
        2: [
          [1,1,0,0,0],
          [1,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,1]
        ],
        3: [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ],
        4: [
            [0,0,0,0,0,0,0,0]
        ]
    }

    for key in testCases:
        print(Solution().maxAreaOfIsland(testCases[key]))