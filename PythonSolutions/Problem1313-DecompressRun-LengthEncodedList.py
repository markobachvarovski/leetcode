from typing import List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            ans.extend([val] * freq)

        return ans


if __name__ == '__main__':

    testCases = {
        1: [1,2,3,4],
        2: [1,1,2,3]
    }

    for key in testCases:
        print(Solution().decompressRLElist(testCases[key]))
