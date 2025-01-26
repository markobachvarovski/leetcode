from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
            return 1 if grid[0][0] == 0 else -1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

        q = deque()
        if grid[0][0] == 0:
            grid[0][0] = 1
            q.append((0, 0, 1))

        while len(q) > 0:
            i, j, length = q.popleft()

            if i == rows - 1 and j == cols - 1:
                return length

            for x, y in directions:
                new_i, new_j = i + x, j + y
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = 1
                    q.append((new_i, new_j, length + 1))

        return -1


if __name__ == '__main__':
    testCases = {
        1: [[0,1],[1,0]], # 2
        2: [[0,0,0],[1,1,0],[1,1,0]], # 4
        3: [[1,0,0],[1,1,0],[1,1,0]], # -1
        4: [[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]] # 14
    }

    for key in testCases:
        print(Solution().shortestPathBinaryMatrix(testCases[key]))
