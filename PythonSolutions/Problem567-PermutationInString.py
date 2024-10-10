from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        l = 0
        r = len(s1) - 1

        while r < len(s2):
            substring = s2[l:r + 1]
            tempCounter = counter.copy()

            for i in substring:
                if i not in tempCounter:
                    break
                if tempCounter[i] == 1:
                    del tempCounter[i]
                else:
                    tempCounter[i] -= 1

            if not tempCounter:
                return True

            l += 1
            r += 1

        return False

if __name__ == '__main__':
    testCases = {
        1: ["ab", "eidbaooo"],
        2: ["ab", "eidboaoo"],
    }

    for key in testCases:
        print(Solution().checkInclusion(testCases[key][0], testCases[key][1]))

