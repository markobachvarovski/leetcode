from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallerArr = []
        pivotArr = []
        largerArr = []

        for num in nums:
            if num < pivot:
                smallerArr.append(num)
            elif num > pivot:
                largerArr.append(num)
            else:
                pivotArr.append(num)

        return smallerArr + pivotArr + largerArr


if __name__ == '__main__':
    testCases = {
        1: [[9,12,5,10,14,3,10], 10],
        2: [[-3,4,3,2], 2]
    }

    for key in testCases:
        print(Solution().pivotArray(testCases[key][0], testCases[key][1]))
