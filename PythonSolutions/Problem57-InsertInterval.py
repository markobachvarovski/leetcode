from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge all overlapping intervals with the new interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Add all the intervals after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


if __name__ == '__main__':
    testCases = {
        1: [[[1,3],[6,9]], [2,5]],
        2: [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]],
    }

    for key in testCases:
        print(Solution().insert(testCases[key][0], testCases[key][1]))
