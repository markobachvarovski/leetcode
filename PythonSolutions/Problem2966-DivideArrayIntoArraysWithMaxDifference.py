from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i + 3])

        return ans

if __name__ == '__main__':
    testCases = {
        1: [[1,3,4,8,7,9,3,5,1], 2],
        2: [[2,4,2,2,5,2], 2],
        3: [[4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 2]
    }

    for key in testCases:
        print(Solution().divideArray(testCases[key][0], testCases[key][1]))
