from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(l, r, nums, target):
            if l == r:
                if not nums or nums[l] != target:
                    return -1
                return l

            midpoint = (l + r) // 2

            if nums[midpoint] == target:
                return midpoint
            elif nums[l] <= nums[midpoint]:  # Left side is sorted
                if nums[l] <= target < nums[midpoint]:
                    return helper(l, midpoint - 1, nums, target)  # Search in the left half
                else:
                    return helper(midpoint + 1, r, nums, target)  # Search in the right half
            else:  # Right side is sorted
                if nums[midpoint] < target <= nums[r]:
                    return helper(midpoint + 1, r, nums, target)  # Search in the right half
                else:
                    return helper(l, midpoint - 1, nums, target)

        return helper(0, len(nums) - 1, nums, target)


if __name__ == '__main__':
    testStrings = {
        1: [[4,5,6,7,0,1,2], 0],
        2: [[4,5,6,7,0,1,2], 3],
    }

    for key in testStrings:
        print(f"The index of {testStrings[key][1]} in {testStrings[key][0]} is: {Solution().search(testStrings[key][0], testStrings[key][1])}")
