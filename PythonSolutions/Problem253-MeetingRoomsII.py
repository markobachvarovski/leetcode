import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timeline = []
        for start, end in intervals:
            timeline.append((start, 1))   # Add 1 room at this time
            timeline.append((end, -1))    # Remove 1 room at this time

        timeline.sort()  # Sort by time

        rooms = 0
        max_rooms = 0

        for time, delta in timeline:
            rooms += delta
            max_rooms = max(max_rooms, rooms)

        return max_rooms


if __name__ == '__main__':
    testCases = {
        1: [[0,30],[5,10],[15,20]],
        2: [[7,10],[2,4]]
    }

    for key in testCases:
        print(Solution().minMeetingRooms(testCases[key]))