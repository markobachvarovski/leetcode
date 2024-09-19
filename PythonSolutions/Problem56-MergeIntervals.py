from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals based on start times
        intervals.sort(key=lambda x: x[0])

        result = []
        currentInterval = intervals[0]

        for i in range(1, len(intervals)):
            if currentInterval[1] >= intervals[i][0]:
                currentInterval[1] = max(currentInterval[1], intervals[i][1])
            else:
                result.append(currentInterval)
                currentInterval = intervals[i]

        result.append(currentInterval)
        return result


if __name__ == '__main__':
    testCases = {
        1: [[1,3],[2,6],[8,10],[15,18]],
        2: [[1,4],[4,5]],
    }

    for key in testCases:
        print(Solution().merge(testCases[key]))
