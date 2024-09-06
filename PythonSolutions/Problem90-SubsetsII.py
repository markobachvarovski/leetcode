from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def getSubset(index):
            if index >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[index])
            getSubset(index + 1)

            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            getSubset(index + 1)

        getSubset(0)
        return res



if __name__ == '__main__':
    testCases = {
        1: [1,2,1],
    }

    for key in testCases:
        print(f"{Solution().subsets(testCases[key])}")
