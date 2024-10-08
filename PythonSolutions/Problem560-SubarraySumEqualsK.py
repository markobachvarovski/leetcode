from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}
        current_sum = 0
        ans = 0

        for num in nums:
            current_sum += num

            if current_sum - k in prefix_sum_count:
                ans += prefix_sum_count[current_sum - k]

            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return ans

if __name__ == '__main__':
    testCases = {
        1: [[1,1,1], 2],
        2: [[1,2,3], 3],
        3: [[1,2,1,2,1], 3],
        4: [[1,-1,0], 0]
    }

    for key in testCases:
        print(Solution().subarraySum(testCases[key][0], testCases[key][1]))

