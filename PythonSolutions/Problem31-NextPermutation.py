from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i < 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    testCases = {
        1: [1, 2, 4, 3],
        2: [1, 3, 2, 4],
        3: [1, 3, 4, 2]
    }

    for key in testCases:
        print(Solution().nextPermutation(testCases[key]))
