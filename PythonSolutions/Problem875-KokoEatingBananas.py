from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            minHrsToEatAllPiles = 0

            for pile in piles:
                minHrsToEatAllPiles += (pile + k - 1) // k

            return minHrsToEatAllPiles <= h

        l = 1
        r = max(piles)

        while l < r:
            midpoint = (l + r) // 2

            if not helper(midpoint):
                l = midpoint + 1
            else:
                r = midpoint

        return l


if __name__ == '__main__':
    testCases = {
        1: [[3,6,7,11], 8],
        2: [[30,11,23,4,20], 5],
        3: [[30,11,23,4,20], 6]
    }

    for key in testCases:
        print(Solution().minEatingSpeed(testCases[key][0], testCases[key][1]))