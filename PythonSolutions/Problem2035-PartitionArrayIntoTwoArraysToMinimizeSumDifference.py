from typing import List
from collections import defaultdict

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        first_half_sums = defaultdict(set)
        second_half_sums = defaultdict(set)

        for i in range(1 << n):
            sum_first = count_first = 0
            sum_second = count_second = 0

            for j in range(n):
                if (i & (1 << j)) != 0:
                    sum_first += nums[j]
                    count_first += 1
                    sum_second += nums[n + j]
                    count_second += 1
                else:
                    sum_first -= nums[j]
                    sum_second -= nums[n + j]

            first_half_sums[count_first].add(sum_first)
            second_half_sums[count_second].add(sum_second)

        answer = float('inf')

        for i in range(n + 1):
            sorted_first_half_sums = sorted(list(first_half_sums[i]))
            sorted_second_half_sums = sorted(list(second_half_sums[n - i]))

            for a in sorted_first_half_sums:
                left, right = 0, len(sorted_second_half_sums) - 1
                target = -a

                while left < right:
                    mid = (left + right) // 2
                    if sorted_second_half_sums[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1

                answer = min(answer, abs(a + sorted_second_half_sums[left]))

                if left > 0:
                    answer = min(answer, abs(a + sorted_second_half_sums[left - 1]))

        return answer


if __name__ == '__main__':
    testCases = {
        1: [3, 2, 5, 1, 6]
    }
    for key in testCases:
        print(Solution().convertArray(testCases[key]))