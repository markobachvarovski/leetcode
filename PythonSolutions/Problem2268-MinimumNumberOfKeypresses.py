from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        sorted_counts = sorted(count.values(), reverse=True)

        pressCount = 0
        letterCount = 0

        for value in sorted_counts:
            pressCount += value * (letterCount // 9 + 1)
            letterCount += 1

        return pressCount

if __name__ == '__main__':
    testCases = {
        1: "apple", # 5
        2: "abcdefghijkl", #15
        3: "aabbccddeeffgg", #14
        4: "", # 0
        5: "aabbccddeeffgghhiijjkkllmmnnoopp" # (16 - 9) * 2 * 2 + 2 * 9 = 46
    }

    for key in testCases:
        print(Solution().minimumKeypresses(testCases[key]))
