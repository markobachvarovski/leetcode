from typing import List

class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        i,j = 0, len(nums) - 1
        numSwaps = 0

        for k in range(len(nums)):
            if nums[k] < nums[i] or (nums[k] == nums[i] and k < i):
                i = k
            if nums[k] > nums[j] or (nums[k] == nums[j] and k > j):
                j = k

        numSwaps += i
        numSwaps += len(nums) - 1 - j
        if j < i:
            numSwaps -= 1

        return numSwaps


if __name__ == '__main__':
    testCases = {
        1: [3, 1, 2, 4],
        2: [5, 4, 3, 2, 1],
        3: [1, 5, 2, 3, 4],
        4: [4, 2, 1, 3],
        5: [1, 2, 3, 4],
        6: [2, 1],
        7: [5],
        8: [4, 5, 1, 2, 3],
        9: [1, 3, 2, 4, 5],
        10: [3, 4, 1, 2, 5]
    }

    for key in testCases:
        print(Solution().minimumSwaps(testCases[key]))