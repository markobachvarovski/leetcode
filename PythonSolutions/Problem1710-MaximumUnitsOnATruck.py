from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxesRemaining = truckSize
        totalUnits = 0

        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for box in boxTypes:
            num, units = box
            totalUnits += min(num, boxesRemaining) * units
            boxesRemaining -= min(num, boxesRemaining)
        return totalUnits


if __name__ == '__main__':
    testCases = {
        1: [[[1,3],[2,2],[3,1]], 4],
        2: [[[5,10],[2,5],[4,7],[3,9]], 10]
    }

    for key in testCases:
        print(Solution().maximumUnits(testCases[key][0], testCases[key][1]))
