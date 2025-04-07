from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        min_length = len(str(low))
        max_length = len(str(high))

        for length in range(min_length, max_length + 1):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)

                if low <= num <= high:
                    result.append(num)

        return result


if __name__ == '__main__':
    testCases = {
        1: [100, 300],
        2: [1000, 13000]
    }

    for key in testCases:
        print(Solution().sequentialDigits(testCases[key][0], testCases[key][1]))
