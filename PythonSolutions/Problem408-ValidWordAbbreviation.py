
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m, n = len(word), len(abbr)
        i = j = x = 0
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == "0" and x == 0:
                    return False
                x = x * 10 + int(abbr[j])
            else:
                i += x
                x = 0
                if i >= m or word[i] != abbr[j]:
                    return False
                i += 1
            j += 1
        return i + x == m and j == n


if __name__ == '__main__':
    testStrings = {
        1: ["substitution", "s10n"],
        2: ["substitution", "substitution"],
        3: ["substitution", "12"],
    }

    for key in testStrings:
        print(Solution().validWordAbbreviation(testStrings[key][0], testStrings[key][1]))
