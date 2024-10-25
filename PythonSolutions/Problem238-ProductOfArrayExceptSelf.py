from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # First pass: Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix  # Store the current prefix in the answer
            prefix *= nums[i]  # Update the prefix for the next index

        # Second pass: Calculate suffix products and multiply with prefix in answer
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix  # Multiply the suffix with the prefix in answer
            suffix *= nums[i]  # Update the suffix for the next index

        return answer


if __name__ == '__main__':
    testCases = {
        1: [1,2,3,4],
        2: [-1,1,0,-3,3]
    }

    for key in testCases:
        print(f"{Solution().productExceptSelf(testCases[key])}")