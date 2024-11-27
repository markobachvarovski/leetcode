from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        paths = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(row: int, col: int, dir: str):
            nonlocal visited
            nonlocal path

            if row not in range(rows)\
                or col not in range(cols)\
                or grid[row][col] == "0"\
                or (row, col) in visited:

                return

            visited.add((row, col))
            path.append(dir)

            dfs(row + 1, col, '1')
            dfs(row - 1, col, '2')
            dfs(row, col + 1, '3')
            dfs (row, col - 1, '4')
            path.append('-'+dir)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    path = []
                    dfs(r, c, "0")
                    paths.add(''.join(path))

        return len(paths)


if __name__ == '__main__':
    testCases = {
        1: [
          ["1","1","0","1","1"],
          ["1","1","0","1","1"],
          ["0","0","0","0","0"],
          ["0","0","1","0","0"]
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