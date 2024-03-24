from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        startIndex = 0
        stopIndex = len(nums) - 1

        if nums[startIndex] > target:
            return startIndex
        elif nums[stopIndex] < target:
            return stopIndex + 1

        while stopIndex - startIndex > 1:
            if (stopIndex - startIndex) % 2 == 0:
                middle = startIndex + (stopIndex-startIndex) // 2
            else:
                middle = startIndex + (stopIndex - startIndex) // 2 + 1

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                stopIndex = middle
            else:
                startIndex = middle

        if nums[startIndex] < target < nums[stopIndex]:
            return stopIndex
        elif stopIndex - startIndex == 0:
            return stopIndex
        else:
            if nums[startIndex] == target:
                return startIndex

            return stopIndex


if __name__ == '__main__':
    testStrings = {
        1: [[1,3,5,6], 5],
        2: [[1,3,5,6], 2],
        3: [[1,3,5,6], 7],
        4: [[1,3], 1],
        5: [[1,3], 3],
        6: [[2,7,8,9,10], 9]
    }

    for key in testStrings:
        print(f"The index of {testStrings[key][1]} in {testStrings[key][0]} is: {Solution().searchInsert(testStrings[key][0], testStrings[key][1])}")
