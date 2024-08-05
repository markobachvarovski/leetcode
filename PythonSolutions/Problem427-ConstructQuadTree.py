# Definition for a Node.
from typing import Optional, List


class QuadTreeNode:
    def __init__(self, val, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> QuadTreeNode:
        if not grid:
            return None

        n = len(grid)
        midpoint = n // 2
        topLeftSameValues, topRightSameValues, bottomLeftSameValues, bottomRightSameValues, wholeGridSameValues = True, True, True, True, True

        dummy = QuadTreeNode(grid[0][0], True, None, None, None, None)
        # Evaluate top left corner
        for i in range(midpoint):
            for j in range(midpoint):
                if grid[i][j] != grid[0][0]:
                    topLeftSameValues = False
                    wholeGridSameValues = False

        # Evaluate top right corner
        for i in range(midpoint):
            for j in range(midpoint, n):
                if grid[i][j] != grid[0][midpoint]:
                    topRightSameValues = False
                if grid[i][j] != grid[0][0]:
                    wholeGridSameValues = False

        # Evaluate bottom left corner
        for i in range(midpoint,n ):
            for j in range(midpoint):
                if grid[i][j] != grid[midpoint][0]:
                    bottomLeftSameValues = False
                if grid[i][j] != grid[0][0]:
                        wholeGridSameValues = False

        for i in range(midpoint, n):
            for j in range(midpoint, n):
                if grid[i][j] != grid[midpoint][midpoint]:
                    bottomRightSameValues = False
                if grid[i][j] != grid[0][0]:
                        wholeGridSameValues = False

        if wholeGridSameValues:
            return dummy

        if topLeftSameValues:
            topLeftNode = QuadTreeNode(grid[0][0], True, None, None, None, None)
        else:
            topLeftNode = self.construct([row[:midpoint] for row in grid[:midpoint]])
        dummy.topLeft = topLeftNode
        dummy.isLeaf = False

        if topRightSameValues:
            topRightNode = QuadTreeNode(grid[0][midpoint], True, None, None, None, None)
        else:
            topRightNode = self.construct([row[midpoint:n] for row in grid[:midpoint]])
        dummy.topRight = topRightNode

        if bottomLeftSameValues:
            bottomLeftNode = QuadTreeNode(grid[midpoint][0], True, None, None, None, None)
        else:
            bottomLeftNode = self.construct([row[:midpoint] for row in grid[midpoint:n]])
        dummy.bottomLeft = bottomLeftNode

        if bottomRightSameValues:
            bottomRightNode = QuadTreeNode(grid[midpoint][midpoint], True, None, None, None, None)
        else:
            bottomRightNode = self.construct([row[midpoint:n] for row in grid[midpoint:n]])
        dummy.bottomRight = bottomRightNode

        return dummy

if __name__ == '__main__':
    testCases = {
        1: [
            [0,1],
            [1,0]
        ],
        2: [
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0],
            [1,1,1,1,0,0,0,0]
        ],
        3: [
            [1,1],
            [1,1]
        ]
    }

    for key in testCases:
        head = Solution().construct(testCases[key])
        # print(f"Key = {key}")
        # while head is not None:
        #     print(head.val)
        #     head = head.next