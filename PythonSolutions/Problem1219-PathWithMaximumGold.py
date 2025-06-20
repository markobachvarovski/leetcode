from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(curr_row, curr_col):
            if not(0 <= curr_row < rows and 0 <= curr_col < cols and grid[curr_row][curr_col] != 0):
                return 0

            temp_val = grid[curr_row][curr_col]
            grid[curr_row][curr_col] = 0

            nbr_1 = dfs(curr_row + 1, curr_col)
            nbr_2 = dfs(curr_row - 1, curr_col)
            nbr_3 = dfs(curr_row, curr_col + 1)
            nbr_4 = dfs(curr_row, curr_col - 1)

            grid[curr_row][curr_col] = temp_val

            return temp_val + max(nbr_1, nbr_2, nbr_3, nbr_4)

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                max_gold = dfs(row, col)
                ans = max(ans, max_gold)

        return ans


if __name__ == '__main__':
    testCases = {
        1: [[0,6,0],[5,8,7],[0,9,0]],
        2: [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    }

    for key in testCases:
        print(Solution().getMaximumGold(testCases[key]))
