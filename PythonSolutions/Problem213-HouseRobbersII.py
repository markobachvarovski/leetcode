from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp_with_first = [0] * (len(nums) - 1)
        dp_with_last = [0] * (len(nums) - 1)

        dp_with_first[0] = nums[0]
        dp_with_last[0] = nums[1]

        dp_with_first[1] = max(nums[1], nums[0])
        dp_with_last[1] = max(nums[2], nums[1])

        for i in range(2, len(nums) - 1):
            dp_with_first[i] = max(dp_with_first[i - 2] + nums[i], dp_with_first[i - 1])
            dp_with_last[i] = max(dp_with_last[i - 2] + nums[i + 1], dp_with_last[i - 1])

        return max(dp_with_first[-1], dp_with_last[-1])

    # Fastest method
    def robWithHelper(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # Rob 1 is with the current house included, rob2 is with the next house included
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

if __name__ == '__main__':
    testCases = {
        1: [2,3,2],
        2: [1,2,3,1],
        3: [1,2,3]
    }

    for key in testCases:
        print(f"{Solution().robWithHelper(testCases[key])}")
