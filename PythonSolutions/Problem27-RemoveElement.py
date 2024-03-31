from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1

        return k

if __name__ == '__main__':
    testArrays = {
        1: [[3,2,2,3], 3],
        2: [[0,1,2,2,3,0,4,2], 2],
    }

    for key in testArrays:
        originalArray = testArrays[key][0].copy()
        print(f"{len(originalArray) - Solution().removeElement(testArrays[key][0], testArrays[key][1])} occurrences of {testArrays[key][1]} were found and removed from {originalArray}")
