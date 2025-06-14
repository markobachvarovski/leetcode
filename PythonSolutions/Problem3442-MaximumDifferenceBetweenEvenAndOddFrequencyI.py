from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = Counter(s)

        max_odd_freq = 0
        min_even_freq = len(s)

        for val in freq_map.values():
            if val % 2 == 1 and val > max_odd_freq:
                max_odd_freq = val

            if val % 2 == 0 and val < min_even_freq:
                min_even_freq = val

        return max_odd_freq - min_even_freq


if __name__ == '__main__':
    testCases = {
        1: "aaaaabbc",
        2: "abcabcab"
    }

    for key in testCases:
        print(Solution().maxDifference(testCases[key]))
