from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


if __name__ == '__main__':
    testCases = {
        1: [1,2,3],
    }

    for key in testCases:
        print(f"{Solution().permute(testCases[key])}")
