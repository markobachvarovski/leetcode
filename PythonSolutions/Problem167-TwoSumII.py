from typing import List
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

if __name__ == '__main__':
    testCases = {
        1: [[-5,-3,0,2,4,6,8], 5],
    }

    for key in testCases:
        print(Solution().twoSum(testCases[key][0], testCases[key][1]))
