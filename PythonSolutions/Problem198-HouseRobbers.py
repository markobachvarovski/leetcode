from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # Rob 1 is with the current house included, rob2 is with the next house included
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2

if __name__ == '__main__':
    testCases = {
        1: [1,2,3,1],
        2: [2,7,9,3,1],
    }

    for key in testCases:
        print(f"{Solution().rob(testCases[key])}")
