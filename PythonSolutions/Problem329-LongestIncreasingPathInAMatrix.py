from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]  # Store the longest path at each cell
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

        # DFS function using a stack (iterative DFS)
        def dfs(i, j):
            if dp[i][j] != 0:  # Already computed
                return dp[i][j]

            max_length = 1  # Minimum path length is 1 (the node itself)
            stack = [(i, j, 1)]  # Stack stores (i, j, path_length)

            while stack:
                x, y, length = stack.pop()

                if dp[x][y] >= length:
                    continue  # Skip if a longer path was already found

                dp[x][y] = max(dp[x][y], length)  # Update dp with the maximum path length

                for dx, dy in directions:  # Explore all 4 directions
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and matrix[x][y] < matrix[nx][ny]:
                        stack.append((nx, ny, length + 1))  # Push the neighbor with incremented length

            return dp[i][j]

        # Run DFS from each cell and compute the longest path
        for i in range(rows):
            for j in range(cols):
                dfs(i, j)

        # The longest path will be the maximum value in the dp array
        return max(max(row) for row in dp)


if __name__ == '__main__':
    testStrings = {
        1: [[9,9,4],[6,6,8],[2,1,1]],
        # 2: ["aabcc", "dbbca", "aadbbbaccc"],
    }

    for key in testStrings:
        print(Solution().longestIncreasingPath(testStrings[key]))
