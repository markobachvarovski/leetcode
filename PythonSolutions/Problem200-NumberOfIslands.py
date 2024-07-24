from collections import deque
from typing import Optional, List, Set


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        numIslands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int):
            nonlocal visited

            if row not in range(rows)\
                or col not in range(cols)\
                or grid[row][col] == "0"\
                or (row, col) in visited:

                return

            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs (row, col - 1)

        def bfs(row: int, col: int):
            queue = deque()
            nonlocal visited

            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()

                for i in [-1, 1]:
                    if row + i in range(rows)\
                        and grid[row + i][col] == '1'\
                        and(row + i, col) not in visited:
                        visited.add((row + i, col))
                        queue.append((row + i, col))

                    if col + i in range(cols) \
                            and grid[row][col + i] == '1' \
                            and (row, col + i) not in visited:
                        visited.add((row, col + i))
                        queue.append((row, col + i))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    numIslands += 1

        return numIslands


if __name__ == '__main__':
    testCases = {
        1: [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ],
        2: [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ],
    }

    for key in testCases:
        print(Solution().numIslands(testCases[key]))