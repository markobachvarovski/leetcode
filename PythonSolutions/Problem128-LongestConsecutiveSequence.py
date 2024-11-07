from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0

        for num in numsSet:
            if num - 1 in numsSet:
                continue

            currNum = num
            while currNum in numsSet:
                currNum += 1

            maxLength = max(maxLength, currNum - num)

        return maxLength

if __name__ == '__main__':
    testCases = {
        1: [100,4,200,1,3,2],
        2: [0,3,7,2,5,8,4,6,0,1]
    }

    for key in testCases:
        print(Solution().longestConsecutive(testCases[key]))