from typing import List


class Solution:
    def minimumTotalRecursive(self, triangle: List[List[int]]) -> int:
        return self.findMinimumPath(triangle, 0, 0)

    def findMinimumPath(self, triangle, row, column):
        if row == len(triangle) - 1:
            return triangle[row][column]

        leftMinimalPath = triangle[row][column] + self.findMinimumPath(triangle, row+1, column)
        rightMinimalPath = triangle[row][column] + self.findMinimumPath(triangle, row+1, column+1)

        return min(leftMinimalPath, rightMinimalPath)

    def minimumTotalIterative(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[row])):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[row][i]
        return dp[0]


if __name__ == '__main__':
    testTriangles = {
        1: [[2],[3,4],[6,5,7],[4,1,8,3]],
        2: [[-10]],
        3: [[-1],[2,3],[1,-1,-3]],
    }

    for key in testTriangles:
        print(
            f"Iterative algorithm - The shortest path in {testTriangles[key]} is: {Solution().minimumTotalIterative(testTriangles[key])}")

    for key in testTriangles:
        print(
            f"Recursive algorithm - The shortest path in {testTriangles[key]} is: {Solution().minimumTotalRecursive(testTriangles[key])}")
