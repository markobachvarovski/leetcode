from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize current_subarray and max_subarray to the first element
        max_product = min_product = global_max_product = nums[0]

        # Start iterating from the second element
        for num in nums[1:]:
            # If num is negative, max and min swap places
            if num < 0:
                max_product, min_product = min_product, max_product

            # Compute the new max_product and min_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            # Update the global maximum product
            global_max_product = max(global_max_product, max_product)

        return global_max_product

if __name__ == '__main__':
    testStrings = {
        1: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        2: [2,3,-2,4],
        3: [-2,0,-1]
    }

    for key in testStrings:
        print(Solution().maxProduct(testStrings[key]))
