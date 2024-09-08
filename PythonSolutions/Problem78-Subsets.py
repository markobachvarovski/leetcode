from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def getSubset(index):
            if index >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[index])
            getSubset(index + 1)

            subset.pop()
            getSubset(index + 1)

        getSubset(0)
        return res



if __name__ == '__main__':
    testCases = {
        1: [1,2,1],
    }

    for key in testCases:
        print(f"{Solution().subsets(testCases[key])}")
