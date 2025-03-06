from typing import List

class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def solve(arr):
            n = len(arr)
            min_ops = [[0] * 1001 for _ in range(n + 1)]

            for i, num in enumerate(arr, 1):
                min_value = float('inf')
                for j in range(1001):
                    if min_value > min_ops[i - 1][j]:
                        min_value = min_ops[i - 1][j]
                    min_ops[i][j] = min_value + abs(num - j)

            return min(min_ops[n])

        return min(solve(nums), solve(nums[::-1]))


if __name__ == '__main__':
    testCases = {
        1: [3, 2, 5, 1, 6]
    }
    for key in testCases:
        print(Solution().convertArray(testCases[key]))