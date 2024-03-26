from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.findMinimumPath(triangle, 0, 0)

    def findMinimumPath(self, triangle, row, column):
        if row == len(triangle) - 1:
            return triangle[row][column]

        leftMinimalPath = triangle[row][column] + self.findMinimumPath(triangle, row+1, column)
        rightMinimalPath = triangle[row][column] + self.findMinimumPath(triangle, row+1, column+1)

        return min(leftMinimalPath, rightMinimalPath)


if __name__ == '__main__':
    testTriangles = {
        1: [[2],[3,4],[6,5,7],[4,1,8,3]],
        2: [[-10]],
        3: [[-1],[2,3],[1,-1,-3]],
    }

    for key in testTriangles:
        print(
            f"The shortest path in {testTriangles[key]} is: {Solution().minimumTotal(testTriangles[key])}")
